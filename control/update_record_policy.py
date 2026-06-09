def evaluate_update_record_policy(action: dict) -> dict:
    if action.get("risk_level") == "high":
        return {
            "decision": "REQUIRE_APPROVAL",
            "reason": "High-risk record update requires approval."
        }

    return {
        "decision": "ALLOW",
        "reason": "Record update admissible."
    }