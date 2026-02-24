WAKE_WORDS = ("hey buddy", "hey buddy alive", "buddy")

def is_wake(text: str) -> bool:
    if not text:
        return False
    t = text.lower().strip()
    return any(w in t for w in WAKE_WORDS)

def strip_wake(text: str) -> str:
    t = (text or "").strip()
    low = t.lower()
    for w in WAKE_WORDS:
        if w in low:
            idx = low.find(w)
            before = t[:idx]
            after = t[idx + len(w):]
            return (before + " " + after).strip()
    return t
