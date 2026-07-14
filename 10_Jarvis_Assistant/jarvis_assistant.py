import pyttsx3
import datetime
import webbrowser

engine = pyttsx3.init()


def speak(text):
    engine.say(text)
    engine.runAndWait()


def wish_me():
    hour = datetime.datetime.now().hour

    if hour < 12:
        speak("Good Morning")

    elif hour < 18:
        speak("Good Afternoon")

    else:
        speak("Good Evening")

    speak("I am Jarvis. How can I help you?")


wish_me()

while True:

    command = input("\nEnter your command: ").lower()

    if "google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif "youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak("Current time is " + current_time)
        print("Current time:", current_time)

    elif "hello" in command:
        speak("Hello. Nice to meet you.")

    elif "exit" in command or "stop" in command:
        speak("Goodbye")
        print("Jarvis stopped.")
        break

    else:
        speak("Sorry, I don't understand that command.")