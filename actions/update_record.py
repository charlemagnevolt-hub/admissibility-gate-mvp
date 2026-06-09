def execute_update_record(action: dict) -> str:
    record_id = action.get("record_id")

    return f"Record {record_id} updated."