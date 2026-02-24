import time
from datetime import datetime
from pathlib import Path

try:
    import cv2
except Exception:
    cv2 = None

from picamera2 import Picamera2


class DualCamera:
    def __init__(self, size=(640, 480)):
        self.camL = Picamera2(0)
        self.camR = Picamera2(1)

        cfgL = self.camL.create_video_configuration(main={"size": size, "format": "RGB888"})
        cfgR = self.camR.create_video_configuration(main={"size": size, "format": "RGB888"})
        self.camL.configure(cfgL)
        self.camR.configure(cfgR)

        self.camL.start()
        self.camR.start()
        time.sleep(1)

    def read(self):
        return self.camL.capture_array(), self.camR.capture_array()

    def stop(self):
        self.camL.stop()
        self.camR.stop()


def snapshot_pair(save_dir="logs"):
    if cv2 is None:
        return None

    cam = DualCamera()
    left, right = cam.read()
    cam.stop()

    both = cv2.hconcat([left, right])

    Path(save_dir).mkdir(parents=True, exist_ok=True)
    name = datetime.now().strftime(f"{save_dir}/vision_%Y%m%d_%H%M%S.jpg")
    cv2.imwrite(name, cv2.cvtColor(both, cv2.COLOR_RGB2BGR))
    return name
