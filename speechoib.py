import speech_recognition as sr
import datetime
import pyttsx3
import webbrowser

# Initialize the speech recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()


def speak(text):
    engine.say(text)
    engine.runAndWait()


def listen():
    with sr.Microphone() as source:
        print("Waiting for your command. Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            statement = recognizer.recognize_google(audio, language='en-in')
            print(f"User said: {statement}\n")
            return statement.lower()
        except sr.UnknownValueError:
            speak("Sorry, I didn't recognize what you said. Can you please repeat for me?")
            return ""
        except sr.RequestError:
            speak("Sorry, my speech service is down.")
            return ""

def get_date():
    now = datetime.datetime.now()
    date = now.strftime("%A, %B %d, %Y")
    speak(f"Today is {date}")


def get_time():
    now = datetime.datetime.now()
    time = now.strftime("%I:%M %p")
    speak(f"At present,the time is {time}")


def search_web(query):
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)
    speak(f"Here is what I found for you{query}")


def run_assistant():
    speak("Hello")
    speak("How can I help you today?")
    while True:
        statement = listen()

        if statement == "":
            continue

        if "time" in statement:
            get_time()
        elif "date" in statement:
            get_date()
        elif "search" in statement:
            speak("What do you want me to search for?")
            search_query = listen()
            if search_query:
                search_web(search_query)
        elif "exit" in statement or "bye" in statement:
            speak("Goodbye!")
            break
        else:
            speak("Sorry, I didn't understand that.")


if __name__ == "__main__":
    run_assistant()
