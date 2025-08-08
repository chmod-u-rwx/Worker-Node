# test_cleanup.py
from __future__ import annotations
import builtins
import signal
import pytest
from src.worker_node.core.cleanup_manager import _cleanup_callbacks, register_cleanup, run_cleanup, handle_signal # pyright: ignore[reportPrivateUsage]
from typing import List


def test_run_cleanup_direct(monkeypatch: pytest.MonkeyPatch) -> None:
    called: List[str] = []

    def fake_cleanup() -> None:
        called.append("done")

    _cleanup_callbacks.clear()
    register_cleanup(fake_cleanup)

    run_cleanup()

    assert called == ["done"]


def test_handle_signal(monkeypatch: pytest.MonkeyPatch) -> None:
    called: List[str] = []
    _cleanup_callbacks.clear()

    def fake_cleanup() -> None:
        called.append("done")

    register_cleanup(fake_cleanup)

    def fake_exit(*args: object, **kwargs: object) -> None:
        raise SystemExit(0)

    monkeypatch.setattr(builtins, "exit", fake_exit)

    with pytest.raises(SystemExit):
        handle_signal(signal.SIGTERM, None)

    assert called == ["done"]
