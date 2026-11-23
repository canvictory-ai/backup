import json
import os
import threading
import uuid
from datetime import datetime, timezone

_LOCK = threading.RLock()
_STAGES = {
    "new": "Mới",
    "contacted": "Đã liên hệ",
    "qualified": "Đã xác định nhu cầu",
    "quoted": "Đã gửi báo giá",
    "negotiating": "Đang thương lượng",
    "won": "Đã chốt",
    "lost": "Không thành công",
    "paused": "Tạm dừng",
}
_EDITABLE = {
    "title", "customer", "contact", "source", "need", "value",
    "stage", "owner", "next_action", "due_date", "note",
}

def _now():
    return datetime.now(timezone.utc).isoformat(timespec="seconds")

def _path(ctx):
    os.makedirs(ctx.data_dir, exist_ok=True)
    return os.path.join(ctx.data_dir, "opportunities.json")

def _load(ctx):
    path = _path(ctx)
    if not os.path.exists(path):
        return []
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    if not isinstance(data, list):
        raise ValueError("Tệp dữ liệu cơ hội không đúng định dạng.")
    return data

def _save(ctx, records):
    path = _path(ctx)
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(records, f, ensure_ascii=False, indent=2)
        f.flush()
        os.fsync(f.fileno())
    os.replace(tmp, path)

def _clean_value(value):
    if value is None or value == "":
        return None
    try:
        number = float(value)
    except (TypeError, ValueError):
        raise ValueError("Giá trị cơ hội phải là số tiền không âm (VND).")
    if number < 0:
        raise ValueError("Giá trị cơ hội không được âm.")
    return int(number) if number.is_integer() else number

def _view(record):
    item = dict(record)
    item["stage_label"] = _STAGES.get(item.get("stage"), item.get("stage", ""))
    return item

def register(ctx):
    def handler(args, ctx):
        op = args.get("op")
        with _LOCK:
            try:
                records = _load(ctx)
            except Exception as e:
                return "ERROR: Không đọc được dữ liệu cơ hội bán hàng: " + str(e)

            if op == "create":
                title = str(args.get("title", "")).strip()
                customer = str(args.get("customer", "")).strip()
                if not title or not customer:
                    return "ERROR: Khi tạo cơ hội cần có tên cơ hội và khách hàng."
                stage = args.get("stage") or "new"
                if stage not in _STAGES:
                    return "ERROR: Giai đoạn không hợp lệ. Dùng một trong: " + ", ".join(_STAGES.keys())
                try:
                    value = _clean_value(args.get("value"))
                except ValueError as e:
                    return "ERROR: " + str(e)
                now = _now()
                record = {
                    "id": "CH-" + datetime.now(timezone.utc).strftime("%y%m%d") + "-" + uuid.uuid4().hex[:6].upper(),
                    "title": title,
                    "customer": customer,
                    "contact": str(args.get("contact") or "").strip(),
                    "source": str(args.get("source") or "").strip(),
                    "need": str(args.get("need") or "").strip(),
                    "value": value,
                    "currency": "VND",
                    "stage": stage,
                    "owner": str(args.get("owner") or "").strip(),
                    "next_action": str(args.get("next_action") or "").strip(),
                    "due_date": str(args.get("due_date") or "").strip(),
                    "note": str(args.get("note") or "").strip(),
                    "archived": False,
                    "created_at": now,
                    "updated_at": now,
                }
                records.append(record)
                try:
                    _save(ctx, records)
                except Exception as e:
                    return "ERROR: Không lưu được cơ hội: " + str(e)
                return json.dumps({"message": "Đã tạo cơ hội bán hàng.", "opportunity": _view(record)}, ensure_ascii=False)

            if op == "list":
                query = str(args.get("query") or "").strip().casefold()
                stage = args.get("stage") or ""
                if stage and stage not in _STAGES:
                    return "ERROR: Giai đoạn không hợp lệ. Dùng một trong: " + ", ".join(_STAGES.keys())
                include_archived = bool(args.get("include_archived", False))
                found = []
                for item in records:
                    if item.get("archived") and not include_archived:
                        continue
                    if stage and item.get("stage") != stage:
                        continue
                    searchable = " ".join(str(item.get(k, "")) for k in ("id", "title", "customer", "contact", "need", "owner", "next_action", "note")).casefold()
                    if query and query not in searchable:
                        continue
                    found.append(_view(item))
                found.sort(key=lambda x: x.get("updated_at", ""), reverse=True)
                return json.dumps({"count": len(found), "stages": _STAGES, "opportunities": found[:100], "truncated": len(found) > 100}, ensure_ascii=False)

            if op in ("get", "update", "archive"):
                oid = str(args.get("id") or "").strip()
                if not oid:
                    return "ERROR: Cần mã cơ hội (id)."
                record = next((item for item in records if item.get("id") == oid), None)
                if record is None:
                    return "ERROR: Không tìm thấy mã cơ hội " + oid
                if op == "get":
                    return json.dumps(_view(record), ensure_ascii=False)
                if op == "archive":
                    record["archived"] = True
                    record["updated_at"] = _now()
                    try:
                        _save(ctx, records)
                    except Exception as e:
                        return "ERROR: Không lưu được thay đổi: " + str(e)
                    return json.dumps({"message": "Đã lưu trữ cơ hội; dữ liệu vẫn được giữ.", "opportunity": _view(record)}, ensure_ascii=False)
                changed = []
                for key in _EDITABLE:
                    if key in args and args[key] is not None:
                        value = args[key]
                        if key == "stage" and value not in _STAGES:
                            return "ERROR: Giai đoạn không hợp lệ. Dùng một trong: " + ", ".join(_STAGES.keys())
                        if key == "value":
                            try:
                                value = _clean_value(value)
                            except ValueError as e:
                                return "ERROR: " + str(e)
                        elif key != "stage":
                            value = str(value).strip()
                        record[key] = value
                        changed.append(key)
                if not changed:
                    return "ERROR: Chưa có trường nào để cập nhật."
                record["updated_at"] = _now()
                try:
                    _save(ctx, records)
                except Exception as e:
                    return "ERROR: Không lưu được thay đổi: " + str(e)
                return json.dumps({"message": "Đã cập nhật: " + ", ".join(changed), "opportunity": _view(record)}, ensure_ascii=False)

            return "ERROR: op phải là create, list, get, update hoặc archive."

    ctx.register_tool(
        name="sales_opportunity",
        description="Quản lý cơ hội bán hàng trong Javis. Tạo cơ hội, lọc danh sách theo khách hàng/giai đoạn, xem chi tiết, cập nhật và lưu trữ. Giá trị tính bằng VND; stage dùng mã new/contacted/qualified/quoted/negotiating/won/lost/paused. Khi tạo cần title và customer.",
        handler=handler,
        min_mode="safe",
        schema={
            "type": "object",
            "properties": {
                "op": {"type": "string", "enum": ["create", "list", "get", "update", "archive"]},
                "id": {"type": "string"},
                "title": {"type": "string"},
                "customer": {"type": "string"},
                "contact": {"type": "string"},
                "source": {"type": "string"},
                "need": {"type": "string"},
                "value": {"type": "number"},
                "stage": {"type": "string", "enum": ["new", "contacted", "qualified", "quoted", "negotiating", "won", "lost", "paused"]},
                "owner": {"type": "string"},
                "next_action": {"type": "string"},
                "due_date": {"type": "string"},
                "note": {"type": "string"},
                "query": {"type": "string"},
                "include_archived": {"type": "boolean"},
            },
            "required": ["op"],
        },
    )
