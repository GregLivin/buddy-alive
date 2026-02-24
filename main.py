#!/usr/bin/env python3
import time
from datetime import datetime

from audio.input import listen
from audio.output import speak
from brain.decision import is_wake, strip_wake
from memory import log_event

ENABLE_VISION = True
VISION_SNAPSHOT_EVERY_SECONDS = 60

def run():
    speak("Buddy Alive is online.")
    log_event("SYSTEM", "Buddy Alive started")
    print("Buddy Alive System Starting...")

    last_snap = 0

    while True:
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{now}] running... (say 'hey buddy')")

        if ENABLE_VISION and (time.time() - last_snap) >= VISION_SNAPSHOT_EVERY_SECONDS:
            last_snap = time.time()
            try:
                from vision.stereo import snapshot_pair
                path = snapshot_pair()
                if path:
                    log_event("VISION", f"snapshot saved: {path}")
            except Exception as e:
                log_event("VISION_ERR", str(e))

        heard = listen(seconds=5)

        if heard:
            print("Heard:", heard)
            log_event("HEARD", heard)

            if is_wake(heard):
                cmd = strip_wake(heard).lower().strip()

                if cmd == "":
                    reply = "Yes. I'm here."
                elif "status" in cmd:
                    reply = "Systems online. Listening and watching."
                elif "take a picture" in cmd or "snapshot" in cmd or "photo" in cmd:
                    reply = "Taking a picture."
                    speak(reply)
                    log_event("SAID", reply)
                    try:
                        from vision.stereo import snapshot_pair
                        path = snapshot_pair()
                        if path:
                            log_event("VISION", f"snapshot saved: {path}")
                            speak("Saved.")
                    except Exception as e:
                        log_event("VISION_ERR", str(e))
                        speak("Camera error.")
                    time.sleep(0.2)
                    continue
                else:
                    reply = f"You said {cmd}"

                speak(reply)
                log_event("SAID", reply)

        time.sleep(0.2)

if __name__ == "__main__":
    run()
