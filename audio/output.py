import os

def speak(text: str):
    safe = text.replace('"', "")
    os.system(f'espeak "{safe}"')
