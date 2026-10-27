import os
from pathlib import Path
import secrets
import subprocess
import sys

import pytest


ROOT = Path(__file__).resolve().parents[1]


@pytest.mark.parametrize(
    "key",
    [None, "", " " * 32, "short", "x" * 31, "your-secret-key",
     "your-secret-key-here", "your-secret-key-here".ljust(64)],
)
def test_startup_rejects_unsafe_signing_key(key):
    env = os.environ.copy()
    env.pop("SECRET_KEY", None)
    if key is not None:
        env["SECRET_KEY"] = key
    result = subprocess.run(
        [sys.executable, "-c", "import app.main"],
        cwd=ROOT, env=env, capture_output=True, text=True, timeout=15,
    )
    assert result.returncode != 0
    assert "Set SECRET_KEY to a unique random value" in result.stderr


def test_configured_key_signs_tokens():
    env = os.environ.copy()
    env["SECRET_KEY"] = secrets.token_hex(32)
    result = subprocess.run(
        [sys.executable, "-c", """
import os
import secrets
import jwt
from fastapi.testclient import TestClient
from app.main import app

with TestClient(app) as client:
    response = client.post('/login', params={'username': 'test', 'password': 'test'})
    assert response.status_code == 200
    token = response.json()['access_token']
    assert jwt.decode(token, os.environ['SECRET_KEY'], algorithms=['HS256'])['sub'] == 'test'
    try:
        jwt.decode(token, secrets.token_hex(32), algorithms=['HS256'])
    except jwt.InvalidSignatureError:
        pass
    else:
        raise AssertionError('Token accepted with the wrong signing key')
"""],
        cwd=ROOT, env=env, capture_output=True, text=True, timeout=15,
    )
    assert result.returncode == 0, result.stderr
