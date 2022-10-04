import speech_recognition as sr
import pyttsx3 as pt
import pywhatkit as pw
import datetime as dt
import wikipedia as wk
import pyjokes as pj

listener = sr.Recognizer()      # listener initialized
speaker = pt.init()             # speaker initialized
def talk(text):
    speaker.say(text)
    speaker.runAndWait()
def take_command():
    try:
        # passing the request using mic
        with sr.Microphone() as req:
            print("Now Listening....")
            voice = listener.listen(req)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'google' in command:
                command = command.replace('google', '')       # replacing the word python
                print(command)
    except:
        print("Something Wrong...")
    return command
def run_google():
    command = take_command()
    print(command)
    if 'play' in command:
        web = command.replace('play', '')
        talk("Playing " + web)
        pw.playonyt(web)
    elif 'time' in command:
        time1 = dt.datetime.now().strftime('%I:%M %p')
        print(time1)
        talk("Current time is " + time1)
    elif "who is" in command:
        about = command.replace('who is ', '')
        info = wk.summary(about)
        talk(info)
    elif "what is" in command:
        about = command.replace('what is ', '')
        info = wk.summary(about)
        talk(info)
    elif "are you single" in command:
        talk("no i am in relation with python. ")
    elif "are you thinking" in command:
        talk("I am thinking about you.")
    elif "joke" in command:
        talk(pj.get_joke())
    else:
        talk("Please repeat again.")
while True:
    try:
        run_google()
    except:
        talk("Something problem with version compatability.")
