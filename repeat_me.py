import os
import speech_recognition as sr

r = sr.Recognizer()

def speak(text: str):
    safe = text.replace('"', "")
    os.system(f'espeak "{safe}"')

def main():
    speak("Say something. I will repeat it.")

    while True:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=0.3)
            print("Listening...")
            audio = r.listen(source, phrase_time_limit=4)

        try:
            text = r.recognize_google(audio)
            print("Heard:", text)
            speak(f"You said {text}")
        except sr.UnknownValueError:
            print("Could not understand.")
        except sr.RequestError as e:
            print("Speech service error:", e)
            speak("Speech service error.")

if __name__ == "__main__":
    main()
