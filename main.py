# pip install pocketsphinx
import speech_recognition as sr
import webbrowser
import pyttsx3
import naatLibrary
import requests
import time
from openai import OpenAI

recognizer = sr.Recognizer()


newsapi= "a701012037624f6fa954d7331cfb07f9"


def speak(text):
    import pyttsx3
    import time

    print("Speaking:", text)

    engine = pyttsx3.init('sapi5')   # force fresh engine
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)

    engine.say(text)
    engine.runAndWait()

    time.sleep(1)

def aiProcess(command):
    client = OpenAI( api_key = "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")

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content":command}
        ]
    )

    return response.choices[0].message.content

def processCommand(c):
    c = c.lower()

    if "open google" in c:
        webbrowser.open("https://google.com")

    elif "open facebook" in c:
        webbrowser.open("https://facebook.com")

    elif "open youtube" in c:
        webbrowser.open("https://youtube.com")

    elif "open linkedin" in c:
        webbrowser.open("https://linkedin.com")

    elif c.startswith("play"):
        klam = " ".join(c.split(" ")[1:])
        link = naatLibrary.naat.get(klam)

        if link:
            webbrowser.open(link)
        else:
            speak("Naat not found")

    elif "news" in c:
        speak("Fetching Pakistan news")

        url = f"https://newsapi.org/v2/top-headlines?country=pk&apiKey={newsapi}"
        r = requests.get(url)

        if r.status_code == 200:
            data = r.json()
            articles = data.get("articles", [])

            if not articles:
                speak("No Pakistan news found, showing international news")
                
                # fallback to US
                url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}"
                r = requests.get(url)
                data = r.json()
                articles = data.get("articles", [])

            for article in articles[:5]:
                title = article.get("title")
                if title:
                    speak(title)
                    time.sleep(1.5)
        else:
            speak("Failed to fetch news")
    else:
        # Let OpenAi handle the request
        output = aiProcess(c)
        speak(output)
            

if __name__ == "__main__":
    speak("Initializing Aura....")
    # Listen for the wake word "Aura"
    # obtain audio from the microphone
    while True:
        try:
            print("Listening for wake word...")

            # STEP 1: Listen for wake word
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source)
                audio = recognizer.listen(source)

            word = recognizer.recognize_google(audio)
            print("Heard:", word)

            if word.lower() == "aura":
                # STEP 2: Speak FIRST (mic is already closed)
                speak("Yes")
                time.sleep(1.5)

                # STEP 3: Now listen for command
                with sr.Microphone() as source:
                    print("Aura Active...")
                    recognizer.adjust_for_ambient_noise(source)
                    audio = recognizer.listen(source)

                command = recognizer.recognize_google(audio)
                print("Command:", command)

                # STEP 4: Execute command (this will speak again)
                processCommand(command)

                # IMPORTANT: pause before next loop
                time.sleep(2)

        except Exception as e:
            print(f"Error: {e}")
            time.sleep(1)
