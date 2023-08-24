"""import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import os
import time

def sptext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("recognizing...")
            data = recognizer.recognize_google(audio)
            print(data)
            return data
        except sr.UnknownValueError:
            print(" Not Understand ")

def Speech_To_Text(x):
    engine = pyttsx3.init() 
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate',120)
    engine.say(x)
    engine.runAndWait()

def main():
        
    #if sptext().lower() in "hey pratik":
        while(True):
            data1 = sptext().lower()

            if "your name" in data1:
                name = "my name is jarvis"
                Speech_To_Text(name)
            elif "old are you" in data1:
                age = "i am two years old"
                Speech_To_Text(age)
            elif "time" in data1:
                time = datetime.datetime.now().strftime("%I%M%p")
                Speech_To_Text(time)
            elif "youtube" in data1:
                brows = webbrowser.open("https://www.youtube.com/")
            elif "joke" in data1:
                joke_1 = pyjokes.get_joke(language="en",category="neutral")
                print(joke_1)
                Speech_To_Text(joke_1)
            elif "play song" in data1:
                add = "C:\\backup\\Python Projects\\Voice Assistant\\Songs"
                listsong = os.listdir(add)
                print(listsong)
                os.startfile(os.path.join(add,listsong[1]))
            elif "exit" in data1:
                Speech_To_Text("thank you")
                break
            #time.sleep(5)



if __name__=="__main__":
    main()"""
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

     