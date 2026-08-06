import structlog
import pytest


@pytest.mark.unit
def test_structlog_emits_to_caplog(caplog):
    """Ensure structlog messages are routed through stdlib logging and captured by caplog."""
    logger = structlog.get_logger("test_structlog")

    # Emit a structured log message
    logger.info("structlog-test-message", foo="bar")

    # caplog should capture the emitted message
    assert "structlog-test-message" in caplog.text or any(
        "structlog-test-message" in record.getMessage() for record in caplog.records
    )
