import speech_recognition as sr
import pyttsx3
import re
# from tkinter import *
import os
import webbrowser
import subprocess


def say():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listning...")
        r.adjust_for_ambient_noise(source,duration=0.2)
        audio = r.listen(source)
        try:
            print("Recognizing...")
            data = r.recognize_google(audio,language='en-in')
            print(data)
            return data
        except:
            print("Please , say that again.")
            return "none"

def speek(a):
    main = pyttsx3.init()
    audio = main.getProperty("voices")
    main.setProperty("voices",audio[0].id)
    b = main.getProperty("rate")
    main.setProperty("rate",130)
    main.say(a)
    main.runAndWait()


if __name__ == "__main__":
    obj = say().lower()
    if re.search(r"(hey|hello) boy",obj) :
        speek("hello anant,how can i help you")
        while True:
            obj2 = say().lower()
            if "your name" in obj2:
                a = "There is no specific name for me,you can call me boy"
                print(a)
                speek(a)
            elif "youtube" in obj2:
                a = obj2
                b = obj2.replace("youtube","").replace(" ","")
                list = ["in","open","search","the"]
                for i in list:
                    if i in b:
                        b = b.replace(i,"")
                c = "youtube.com/"+b
                webbrowser.open(c)
            elif "whatsapp" in obj2:
                subprocess.Popen(["cmd","/c","start whatsapp:"],shell = False)
            elif "code" in obj2:
                os.startfile("C:\\Users\\ANANT\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\\Visual Studio Code.lnk")
            elif ("search" in obj2 or "open" in obj2):
                a = obj2
                b = obj2.replace(" ","")
                list = ["in","open","search","the","browser","google","chrome"]
                for i in list:
                    if i in b:
                        b = b.replace(i,"")
                webbrowser.open(b+".com")

            elif "exit" in obj2:
                print("Exiting..")
                speek("exiting")
                exit()


                


