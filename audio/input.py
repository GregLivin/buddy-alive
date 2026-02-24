import speech_recognition as sr

r = sr.Recognizer()

def listen(seconds: int = 4, device_index=None):
    with sr.Microphone(device_index=device_index) as source:
        r.adjust_for_ambient_noise(source, duration=0.3)
        audio = r.listen(source, phrase_time_limit=seconds)

    try:
        return r.recognize_google(audio)
    except sr.UnknownValueError:
        return None
    except sr.RequestError as e:
        return f"[speech service error: {e}]
