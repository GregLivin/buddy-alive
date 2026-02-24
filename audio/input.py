import speech_recognition as sr

r = sr.Recognizer()

MIC_INDEX = 0  # USB Microphone: Audio (hw:0,0)

def listen(seconds: int = 5) -> str | None:
    with sr.Microphone(device_index=MIC_INDEX, sample_rate=16000) as source:
        r.dynamic_energy_threshold = True
        r.pause_threshold = 0.8
        r.non_speaking_duration = 0.4
        r.adjust_for_ambient_noise(source, duration=0.8)
        print("Listening...")
        audio = r.listen(source, timeout=6, phrase_time_limit=seconds)

    try:
        return r.recognize_google(audio)
    except sr.UnknownValueError:
        return None
    except sr.RequestError as e:
        return f"[speech service error: {e}]"
