def execute_send_email(action: dict) -> str:
    recipient = action.get("recipient")
    subject = action.get("subject", "No subject")

    return f"Email sent to {recipient} with subject: {subject}"
