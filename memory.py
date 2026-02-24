from pathlib import Path
from datetime import datetime

LOG_DIR = Path("logs")

def log_event(kind: str, text: str):
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    day = datetime.now().strftime("%Y-%m-%d")
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    path = LOG_DIR / f"conversation_{day}.log"
    with path.open("a", encoding="utf-8") as f:
        f.write(f"[{ts}] {kind}: {text}\n")
