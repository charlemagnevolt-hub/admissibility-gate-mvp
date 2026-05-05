from control.policy import evaluate_email_policy


def evaluate_admissibility(action: dict) -> dict:
    action_type = action.get("type")

    if action_type == "send_email":
        return evaluate_email_policy(action)

    return {
        "decision": "BLOCK",
        "reason": f"Unsupported action type: {action_type}"
    }
