# 🤖 Buddy Alive

Buddy Alive is a Raspberry Pi 5 powered humanoid robot system.

It includes:
- Voice recognition (USB microphone)
- Text-to-speech (espeak)
- Dual stereo vision (2x Pi Camera Module 3)
- Wake word detection ("hey buddy")
- Persistent conversation logging
- Automatic stereo image snapshots
- GitHub version control

---

## 🧱 Hardware

- Raspberry Pi 5  
- 2x Pi Camera Module 3 (IMX708 Noir)  
- USB Microphone  
- USB Speaker  
- 3D printed Lil Buddy head  

---

## 📁 Project Structure

buddy-alive/
│
├── main.py              # Core system loop  
├── memory.py            # Logging system  
│  
├── audio/  
│   ├── input.py         # Speech recognition  
│   └── output.py        # Text-to-speech  
│  
├── brain/  
│   └── decision.py      # Wake word + command logic  
│  
├── vision/  
│   └── stereo.py        # Dual camera capture  
│  
├── logs/                # Images + conversation logs  
│  
└── .venv/               # Virtual environment  

---

## 🚀 How To Run Buddy

1. Open terminal on Raspberry Pi  
2. Navigate to project:

cd ~/projects/buddy-alive

3. Activate virtual environment:

source .venv/bin/activate

4. Start Buddy:

python main.py

---

## 🗣 Voice Commands

Wake word required.

Examples:

hey buddy  
hey buddy status  
hey buddy take a picture  

---

## 👀 Vision System

- Dual cameras capture stereo images  
- Automatic snapshot every 60 seconds  
- Manual snapshot via voice command  
- Images saved to:

logs/vision_YYYYMMDD_HHMMSS.jpg

---

## 📝 Memory Logging

All events are logged daily in:

logs/conversation_YYYY-MM-DD.log

Logged events:
- SYSTEM startup  
- HEARD speech  
- SAID responses  
- VISION snapshots  

---

## 🔧 Dependencies

System packages:

sudo apt install python3-picamera2 python3-opencv flac espeak

Python packages (inside .venv):

pip install SpeechRecognition PyAudio

---

## 🛠 Optional Start Shortcut

Create shortcut:

nano ~/start-buddy.sh

Paste:

#!/bin/bash
cd ~/projects/buddy-alive
source .venv/bin/activate
python main.py

Make executable:

chmod +x ~/start-buddy.sh

Run anytime:

~/start-buddy.sh

---

## 📌 Current Version

Buddy Alive v0.3

Features:
- Wake word detection  
- Stereo image capture  
- Voice commands  
- Persistent logs  
- GitHub-managed development  

---

## 🔮 Future Upgrades

- Offline Whisper speech engine  
- Face detection  
- Object recognition  
- Servo head movement  
- Emotional response system  
- Web dashboard  
- Auto-start on boot  

---

## 👨🏾‍💻 Creator

Greg Livingston Jr.  
AI & Robotics Engineering  
Houston, TX  
