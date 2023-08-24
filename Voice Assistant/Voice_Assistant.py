import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import os
import time

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("Recognizing...")
            data = recognizer.recognize_google(audio)
            print("You said:", data)
            return data.lower()
        except sr.UnknownValueError:
            print("Could not understand audio")

def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 120)
    engine.say(text)
    engine.runAndWait()

def main():
        while True:
            command = listen()

            if "hey jarvis" in command:
                speak("How can I assist you?")
            elif "your name" in command:
                speak("My name is Jarvis")
            elif "how old are you" in command:
                speak("I am a virtual assistant")
            elif "time" in command:
                current_time = datetime.datetime.now().strftime("%I:%M %p")
                speak("The current time is " + current_time)
            elif "YouTube" in command:
                webbrowser.open("https://www.youtube.com/")
            elif "joke" in command:
                joke = pyjokes.get_joke(language="en", category="neutral")
                print(joke)
                speak(joke)
            elif "play song" in command:
                songs_folder = "C:\\backup\\Python Projects\\Voice Assistant\\Songs"
                song_list = os.listdir(songs_folder)
                if song_list:
                    os.startfile(os.path.join(songs_folder, song_list[0]))
                else:
                    speak("No songs found in the folder")
            elif "exit" in command:
                speak("Thank you. Goodbye!")
                break
            else:
                speak("Sorry, I don't understand that command. Please try again.")

if __name__ == "__main__":
    main()

     