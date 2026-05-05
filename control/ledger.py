import json
from datetime import datetime, timezone
from pathlib import Path


LEDGER_PATH = Path("logs/ledger.json")


def write_ledger_entry(action: dict, decision: dict) -> None:
    LEDGER_PATH.parent.mkdir(parents=True, exist_ok=True)

    entry = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "action": action,
        "decision": decision
    }

    if LEDGER_PATH.exists():
        with open(LEDGER_PATH, "r", encoding="utf-8") as file:
            try:
                ledger = json.load(file)
            except json.JSONDecodeError:
                ledger = []
    else:
        ledger = []

    ledger.append(entry)

    with open(LEDGER_PATH, "w", encoding="utf-8") as file:
        json.dump(ledger, file, indent=2)
