#!/usr/bin/env python3
import time
from datetime import datetime

def run():
    print("Buddy Alive System Starting...")
    while True:
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{now}] Buddy is running...")
        time.sleep(5)

if __name__ == "__main__":
    run()
