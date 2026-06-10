def evaluate_api_policy(action: dict) -> dict:
    if action.get("risk_level") == "high":
        return {
            "decision": "REQUIRE_APPROVAL",
            "reason": "High-risk API call requires approval."
        }

    if not action.get("endpoint"):
        return {
            "decision": "BLOCK",
            "reason": "Missing API endpoint."
        }

    return {
        "decision": "ALLOW",
        "reason": "API call admissible."
    }