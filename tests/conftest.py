"""Shared test fixtures for PathReview."""

import pytest

# Ensure structlog is configured to route through the standard library logging
# so pytest's caplog can capture messages emitted via structlog.
from core.logging import configure_logging


@pytest.fixture(scope="session", autouse=True)
def enable_structlog_logging():
    """Session-scoped autouse fixture to configure structlog for tests.

    This sets up structlog to use the stdlib LoggerFactory and configures
    the root logging handler so pytest.caplog can capture emitted messages.
    """
    configure_logging()
    yield


@pytest.fixture
def sample_resume_text() -> str:
    """Return a sample resume text for testing."""
    return """
    Jane Doe
    Software Engineer
    jane.doe@example.com | github.com/janedoe

    Experience:
    - Software Engineer at TechCorp (2022-2024)
      Built REST APIs using Python and FastAPI.

    Education:
    - B.S. Computer Science, State University (2022)

    Skills: Python, JavaScript, React, PostgreSQL, Docker
    """


@pytest.fixture
def sample_readme_text() -> str:
    """Return a sample README text for testing."""
    return """
    # Weather App
    A weather forecasting application built with React and OpenWeatherMap API.

    ## Features
    - Current weather display
    - 5-day forecast
    - Location search

    ## Tech Stack
    - React 18
    - TypeScript
    - Tailwind CSS
    - OpenWeatherMap API
    """
