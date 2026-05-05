def evaluate_email_policy(action: dict) -> dict:
    recipient_type = action.get("recipient_type")
    contains_sensitive_data = action.get("contains_sensitive_data", False)
    approved_by_human = action.get("approved_by_human", False)

    if recipient_type == "external" and contains_sensitive_data and not approved_by_human:
        return {
            "decision": "REQUIRE_APPROVAL",
            "reason": "External email contains sensitive data and has no human approval."
        }

    if recipient_type == "external" and action.get("risk_level") == "high":
        return {
            "decision": "REQUIRE_APPROVAL",
            "reason": "High-risk external email requires approval."
        }

    if action.get("recipient") is None:
        return {
            "decision": "BLOCK",
            "reason": "Missing recipient."
        }

    return {
        "decision": "ALLOW",
        "reason": "Action is admissible under current policy."
    }
