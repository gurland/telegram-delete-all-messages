"""Regression tests for chat-selection input handling in cleaner.py.

cleaner.py performs network I/O at import time, so ``pyrogram`` and
``qr_auth`` are stubbed before import and a throwaway ``cache`` file is
pre-created (and removed again after the test session).
"""

import asyncio
import json
import os
import sys
import types
from pathlib import Path
from types import SimpleNamespace

import pytest

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))
os.environ.setdefault("API_ID", "12345")
os.environ.setdefault("API_HASH", "abcdef")


class _StubClient:
    def __init__(self, *args, **kwargs):
        pass

    def run(self, *args, **kwargs):
        return None


def _install_stubs():
    chat_types = SimpleNamespace(GROUP="group", SUPERGROUP="supergroup", CHANNEL="channel")
    enums = SimpleNamespace(ChatType=chat_types)

    errors = types.ModuleType("pyrogram.errors")
    for exc_name in (
        "AuthKeyInvalid",
        "AuthKeyUnregistered",
        "FloodWait",
        "SessionExpired",
        "SessionRevoked",
        "UnknownError",
    ):
        setattr(errors, exc_name, type(exc_name, (Exception,), {}))

    pyrogram = types.ModuleType("pyrogram")
    pyrogram.Client = _StubClient
    pyrogram.enums = enums
    pyrogram.raw = SimpleNamespace()
    pyrogram.errors = errors

    qr_auth = types.ModuleType("qr_auth")
    qr_auth.login_with_qr = lambda app: None

    sys.modules["pyrogram"] = pyrogram
    sys.modules["pyrogram.errors"] = errors
    sys.modules["qr_auth"] = qr_auth
    return chat_types


CHAT_TYPES = _install_stubs()

CACHE = REPO / "cache"
CREATED_CACHE = not CACHE.exists()
if CREATED_CACHE:
    CACHE.write_text(
        json.dumps({"API_ID": "12345", "API_HASH": "abcdef"}), encoding="utf-8"
    )

import cleaner  # noqa: E402


@pytest.fixture(scope="session", autouse=True)
def _cleanup_cache():
    yield
    if CREATED_CACHE and CACHE.exists():
        CACHE.unlink()


def _group(chat_id=1, title="Group One"):
    return SimpleNamespace(id=chat_id, title=title, username="g1")


def _run_selection(monkeypatch, user_input, groups):
    async def fake_get_groups(self):
        return (groups, {})

    monkeypatch.setattr(cleaner.Cleaner, "get_groups", fake_get_groups)
    monkeypatch.setattr("builtins.input", lambda *args, **kwargs: user_input)
    instance = cleaner.Cleaner()
    asyncio.run(instance.select_groups())
    return instance


def test_select_groups_rejects_non_numeric_input(monkeypatch, capsys):
    with pytest.raises(SystemExit) as exc_info:
        _run_selection(monkeypatch, "abc", [_group()])
    assert exc_info.value.code == -1
    assert "Invalid option selected" in capsys.readouterr().out


def test_select_groups_rejects_empty_input(monkeypatch, capsys):
    with pytest.raises(SystemExit) as exc_info:
        _run_selection(monkeypatch, "", [_group()])
    assert exc_info.value.code == -1
    assert "Invalid option selected" in capsys.readouterr().out


def test_select_groups_accepts_valid_choice(monkeypatch):
    group = _group()
    instance = _run_selection(monkeypatch, "1", [group])
    assert [chat.id for chat in instance.chats] == [group.id]
