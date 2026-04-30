# F.R.I.D.A.Y — AI Chatbot Desktop App

> A Python-based desktop AI chatbot with voice input,
> speech output, and a self-learning system.

---

## Features
- Text-based chat interface
- Voice recognition (say "Friday [command]")
- Text-to-speech responses
- Self-learning: teach the bot new answers on the fly
- Import Q&A data from CSV or TXT files
- Open websites, play YouTube, Google search
- Take screenshots on command
- Login & Sign-up system

---

## Project Structure
```
friday-chatbot/
├── login.py
├── signup.py
├── main_app.py
├── speech_output.py
├── voice_recoginition.py
├── chatbot_data.txt
├── sample_data.txt
├── requirements.txt
├── friday_ai.png
├── chat_bot.jpg
├── login_logo.png
├── user.png
└── README.md
```

---

## Getting Started

### 1. Clone the repo
```bash
git clone https://github.com/nikhileshh02/friday-chatbot.git
cd friday-chatbot
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

> PyAudio on Windows:
> `pip install pipwin` then `pipwin install pyaudio`

### 3. Run
```bash
python login.py
```

---

## Built With
Python, Tkinter, Pillow, pyttsx3, SpeechRecognition, pywhatkit, pyautogui, pandas

---

## Author
**Nikhilesh Chouhan** — [GitHub](https://github.com/nikhileshh02)

## License
MIT
