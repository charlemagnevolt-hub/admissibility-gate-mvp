def execute_call_api(action: dict) -> str:
    endpoint = action.get("endpoint")

    return f"API call executed against endpoint: {endpoint}"