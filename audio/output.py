import os

def speak(text: str):
    safe = (text or "").replace('"', "")
    os.system(f'espeak "{safe}"')
