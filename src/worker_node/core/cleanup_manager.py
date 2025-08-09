# cleanup_manager.py
import signal
import atexit
from typing import Any, Callable, List, NoReturn, Optional

_cleanup_callbacks: List[Callable[[], None]] = []

def register_cleanup(func: Callable[[], None]) -> None:
    _cleanup_callbacks.append(func)

def run_cleanup() -> None:
    for func in _cleanup_callbacks:
        try:
            func()
        except Exception as e:
            print(f"Error during cleanup: {e}")

def handle_signal(signum: int, _: Optional[Any]) -> NoReturn:
    run_cleanup()
    raise SystemExit(0)

atexit.register(run_cleanup)
signal.signal(signal.SIGINT, handle_signal)
signal.signal(signal.SIGTERM, handle_signal)
