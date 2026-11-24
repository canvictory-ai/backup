"""Report likely missed technical questions in TESTBOT through scheduler stdout."""
import json
import os
from pathlib import Path
import re
import sqlite3
import time

GROUP = "5049425754926522263"
ACCOUNT = "zalo_personal:7b712729db57"
DB = Path("/data/state/customer_conversations.sqlite3")
LOG = Path("/data/state/chatbot-logs/bot_dac5c94415.jsonl")
STATE = Path(os.environ.get("JAVIS_BRAIN_ROOT", Path(__file__).resolve().parents[2])) / "loop-data/testbot-review.json"
TOPIC = re.compile(r"\b(máy in|canon|brother|pantum|epson|xprinter|laserjet|giấy trắng|kẹt giấy|hộp mực|wifi|wi-fi|modem|router|camera|laptop|máy tính)\b", re.I)
QUESTION = re.compile(r"\?|lỗi gì|bị gì|làm sao|cách|kiểm tra|xử lý|khắc phục", re.I)


def metadata(row):
    return json.loads(row["metadata_json"] or "{}")


def normalized(text):
    return " ".join(re.sub(r"[\s*_]+", " ", text).split()).casefold()


def review():
    now = time.time()
    if not STATE.exists():
        return {"started": now, "reported": {}}, []
    saved = json.loads(STATE.read_text())
    earliest = max(saved["started"], now - 86400)
    already = {key: when for key, when in saved["reported"].items() if when >= earliest}
    with sqlite3.connect(DB.as_uri() + "?mode=ro", uri=True, timeout=5) as conn:
        conn.row_factory = sqlite3.Row
        messages = conn.execute(
            "SELECT m.* FROM messages m JOIN conversations c ON c.id=m.conversation_id "
            "WHERE c.external_chat_id=? AND c.channel_account_id=? AND m.created_at>=? "
            "ORDER BY m.created_at,m.id", (GROUP, ACCOUNT, earliest),
        ).fetchall()
    outgoing = [m for m in messages if m["sender_type"] in ("human", "ai") and
                (m["sender_type"] == "human" or
                 metadata(m).get("zalo_delivery", {}).get("state") in ("accepted", "sent", "delivered"))]
    quoted = {str((metadata(m).get("replyTo") or {}).get("msgId") or "") for m in outgoing}
    turns = []
    if outgoing and LOG.exists():
        with LOG.open("rb") as stream:
            stream.seek(max(0, LOG.stat().st_size - 1024 * 1024))
            for line in stream:
                try:
                    turn = json.loads(line)
                except (ValueError, UnicodeError):
                    continue
                if turn.get("chat_id") == GROUP and turn.get("ts", 0) >= earliest:
                    turns.append(turn)

    alerts = []
    for m in messages:
        key = m["external_message_id"]
        body = m["text"] or ""
        when = m["created_at"]
        if (not key or key in already or key in quoted or m["sender_type"] != "customer"
                or m["message_type"] != "text" or when > now - 120
                or not TOPIC.search(body) or not QUESTION.search(body)):
            continue
        answered = any(
            normalized(turn.get("hoi") or "") == normalized(body)
            and when <= turn["ts"] <= when + 180
            and any(abs(reply["created_at"] - turn["ts"]) <= 20 and
                    normalized(turn.get("dap") or "") and
                    normalized(turn["dap"]) in normalized(reply["text"] or "") for reply in outgoing)
            for turn in turns
        )
        if not answered and len(alerts) < 6:
            alerts.append((key, " ".join(body.split())[:240]))
            already[key] = when
    return {"started": saved["started"], "reported": already}, alerts


def main():
    state, alerts = review()
    STATE.parent.mkdir(parents=True, exist_ok=True)
    tmp = STATE.with_suffix(".tmp")
    tmp.write_text(json.dumps(state), encoding="utf-8")
    tmp.replace(STATE)
    if alerts:
        print("TESTBOT · Tin kỹ thuật chờ hơn 2 phút, chưa thấy phản hồi được gắn hoặc đối chiếu:")
        for key, body in alerts:
            print(f"- {body}  (tin {key})")


if __name__ == "__main__":
    main()
