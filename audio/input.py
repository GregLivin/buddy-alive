import speech_recognition as sr

r = sr.Recognizer()

MIC_INDEX = 0          # USB Microphone: Audio (hw:0,0)
SAMPLE_RATE = 48000    # Supported: 44100 or 48000

def listen(seconds: int = 5) -> str | None:
    """
    Listen from USB mic and return recognized text, or None.
    This version avoids crashing if the audio stream fails.
    """
    try:
        with sr.Microphone(device_index=MIC_INDEX, sample_rate=SAMPLE_RATE) as source:
            r.dynamic_energy_threshold = True
            r.pause_threshold = 0.8
            r.non_speaking_duration = 0.4

            print(f"Listening... (rate={SAMPLE_RATE})")
            r.adjust_for_ambient_noise(source, duration=0.6)
            audio = r.listen(source, timeout=6, phrase_time_limit=seconds)
    except Exception as e:
        print(f"[MIC ERROR] {e}")
        return None

    try:
        return r.recognize_google(audio)
    except sr.UnknownValueError:
        return None
    except sr.RequestError as e:
        return f"[speech service error: {e}]"
