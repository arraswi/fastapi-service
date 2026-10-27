import os
import secrets

import pytest


# Generate a key only for this test process, before importing the application.
os.environ["SECRET_KEY"] = secrets.token_hex(32)


@pytest.fixture(autouse=True)
def reset_application_state():
    from app.main import items, users

    items.clear()
    users.clear()
    yield
    items.clear()
    users.clear()
