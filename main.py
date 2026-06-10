import json
import sys

from control.admissibility import evaluate_admissibility
from control.ledger import write_ledger_entry
from actions.send_email import execute_send_email
from actions.update_record import execute_update_record
from actions.call_api import execute_call_api


def load_action(path: str) -> dict:
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def execute_action(action: dict) -> str:
    action_type = action.get("type")

    if action_type == "send_email":
        return execute_send_email(action)

    if action_type == "update_record":
        return execute_update_record(action)

    if action_type == "call_api":
        return execute_call_api(action)

    return f"Unsupported action type: {action_type}"


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python main.py examples/email_external_sensitive.json")
        sys.exit(1)

    action_path = sys.argv[1]
    action = load_action(action_path)

    decision = evaluate_admissibility(action)

    print(f"Decision: {decision['decision']}")
    print(f"Reason: {decision['reason']}")

    if decision["decision"] == "ALLOW":
        result = execute_action(action)
        print(result)
    else:
        print("Action was not executed.")

    write_ledger_entry(action, decision)
    print("Ledger entry written.")


if __name__ == "__main__":
    main()