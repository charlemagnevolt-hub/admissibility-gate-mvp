from control.policy import evaluate_email_policy
from control.update_record_policy import evaluate_update_record_policy
from control.api_policy import evaluate_api_policy


def evaluate_admissibility(action: dict) -> dict:
    action_type = action.get("type")

    if action_type == "send_email":
        return evaluate_email_policy(action)

    if action_type == "update_record":
        return evaluate_update_record_policy(action)

    if action_type == "call_api":
        return evaluate_api_policy(action)

    return {
        "decision": "BLOCK",
        "reason": f"Unsupported action type: {action_type}"
    }