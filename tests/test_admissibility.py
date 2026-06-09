from control.admissibility import evaluate_admissibility


def test_internal_email_is_allowed():
    action = {
        "type": "send_email",
        "recipient": "team@company.local",
        "recipient_type": "internal",
        "contains_sensitive_data": False,
        "approved_by_human": False
    }

    decision = evaluate_admissibility(action)

    assert decision["decision"] == "ALLOW"


def test_external_sensitive_email_requires_approval():
    action = {
        "type": "send_email",
        "recipient": "client@example.com",
        "recipient_type": "external",
        "contains_sensitive_data": True,
        "approved_by_human": False
    }

    decision = evaluate_admissibility(action)

    assert decision["decision"] == "REQUIRE_APPROVAL"


def test_missing_recipient_is_blocked():
    action = {
        "type": "send_email",
        "recipient": None,
        "recipient_type": "external",
        "contains_sensitive_data": False,
        "approved_by_human": False
    }

    decision = evaluate_admissibility(action)

    assert decision["decision"] == "BLOCK"


def test_low_risk_record_update_is_allowed():
    action = {
        "type": "update_record",
        "record_id": "customer-123",
        "risk_level": "low"
    }

    decision = evaluate_admissibility(action)

    assert decision["decision"] == "ALLOW"


def test_high_risk_record_update_requires_approval():
    action = {
        "type": "update_record",
        "record_id": "customer-999",
        "risk_level": "high"
    }

    decision = evaluate_admissibility(action)

    assert decision["decision"] == "REQUIRE_APPROVAL"


def test_unsupported_action_type_is_blocked():
    action = {
        "type": "delete_resource",
        "resource_id": "file-123"
    }

    decision = evaluate_admissibility(action)

    assert decision["decision"] == "BLOCK"