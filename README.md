# 🎙️ Aura — AI Voice Assistant

A Python-based voice-activated AI assistant that listens, 
thinks, and responds.

![Python](https://img.shields.io/badge/Python-3.10-blue)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--3.5-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## 🚀 What Aura Can Do

- 🎙️ Wake up when you say **"Aura"**
- 🌐 Open Google, YouTube, Facebook, LinkedIn by voice
- 📰 Fetch and read **live Pakistan news** out loud
- 🕌 Play **naats by name** from a custom library
- 🤖 Answer any question using **ChatGPT (GPT-3.5)**

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python 3.10 | Core language |
| SpeechRecognition | Voice input / wake word |
| pyttsx3 | Text to speech output |
| OpenAI API | GPT-3.5 for open questions |
| NewsAPI | Live Pakistan news |
| webbrowser | Open websites by voice |

---

## ⚙️ Setup & Installation

### 1. Clone the repository
git clone https://github.com/YOUR_USERNAME/Aura-Voice-Assistant.git
cd Aura-Voice-Assistant

### 2. Create a virtual environment
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # Mac/Linux

### 3. Install dependencies
pip install -r requirements.txt

### 4. Add your API keys
Create a .env file in the project folder:
OPENAI_API_KEY=your_openai_key_here
NEWS_API_KEY=your_newsapi_key_here

### 5. Run Aura
python main.py

---

## 🎮 How to Use

1. Run the program
2. Wait for **"Initializing Aura..."**
3. Say **"Aura"** — she replies **"Yes"**
4. Give your command:

| Say This | Aura Does This |
|---|---|
| "Open YouTube" | Opens YouTube |
| "Open Google" | Opens Google |
| "News" | Reads Pakistan headlines |
| "Play [naat name]" | Plays that naat |
| Any question | Answers via ChatGPT |

---

## 🐛 Troubleshooting

**Python version conflict?**
Use a virtual environment with Python 3.10:
python -m venv venv --python=python3.10

**Microphone not detected?**
pip install pyaudio
Make sure mic is set as default in Windows sound settings.

**pyttsx3 engine crash?**
Make sure you are using sapi5 engine (Windows only).

---

## 📚 Learning Credits

- **CodeWithHarry** — YouTube channel that made Python practical
- **Sir Zafar Iqbal** — Mentor who made every concept click
- Built after completing MSCS in 2021

---

## 🙋 Author

**Hafiz Ahmad Adil**
- LinkedIn: [your linkedin url]
- GitHub: [your github url]

---

## 📄 License
MIT License — free to use and modify
