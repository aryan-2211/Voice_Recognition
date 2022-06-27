import pyttsx3
import speech_recognition
import datetime
import pyautogui
import random
import webbrowser
import os
import speedtest
from translate import translategl

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate", 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 250
        audio = r.listen(source, 0, 4)

    try:
        print("Understanding...")
        query = r.recognize_google(audio, language = 'en-in')
        print(f"You said : {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    
    return query

if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if "wake up" in query:
            from greetMe import greet
            greet()

            while True:
                query = takeCommand().lower()
                if "go to sleep" in query:
                    speak("Ok sir, You can call me anytime")
                    break
                elif "hello" in query:
                    speak("Hello sir, how are you?")
                elif "fine" in query:
                    speak("that's great, sir")
                elif "how are you" in query:
                    speak("Perfect, sir")
                elif "thank you" in query:
                    speak("you are welcome, sir")
                elif "pause" in query:
                    pyautogui.press("k")
                    speak("Video paused")
                elif "play" in query:
                    pyautogui.press("k")
                    speak("Video played")
                elif "mute" in query:
                    pyautogui.press("m")
                elif "volume up" in query:
                    from volume import volumeUp
                    speak("Turning volume up, Sir")
                    volumeUp()
                elif "volume down" in query:
                    from volume import volumeDown
                    speak("Turning volume down, Sir")
                    volumeDown()
                elif "open" in query:
                    from dictApp import openappweb
                    openappweb(query)
                elif "close" in query:
                    from dictApp import closeappweb
                    closeappweb(query)
                elif "google" in query:
                    from searchNow import searchGoogle
                    searchGoogle(query)
                elif "youtube" in query:
                    from searchNow import searchYT
                    searchYT(query)
                elif "the time" in query:
                    time = datetime.datetime.now().strftime("%H:%M")
                    speak(f"Sir, the time is {time}")
                elif "remember that" in query:
                    msg = query.replace("remember that", "")
                    msg = query.replace("coco", "")
                    speak("You told me to"+msg)
                    rem = open("remMessage.txt", "a")
                    rem.write(msg)
                    rem.close()
                elif "what do you remember" in query:
                    rem = open("remMessage.txt", "r")
                    speak("You told me to" + rem.read())
                elif "tired" in query:
                    speak("Playing your favourite song")
                    a = (1,2,3,4,5)
                    b = random.choice(a)
                    if b == 1:
                        webbrowser.open("https://www.youtube.com/watch?v=9M2F6EaU-kM&list=RDDvIauQX0NvE&index=2")
                    elif b == 2:
                        webbrowser.open("https://www.youtube.com/watch?v=DvIauQX0NvE&list=RDDvIauQX0NvE&index=1")
                    elif b == 3:
                        webbrowser.open("https://www.youtube.com/watch?v=wlaZSx6tqRo&list=RDDvIauQX0NvE&index=5")
                    else:
                        webbrowser.open("https://www.youtube.com/watch?v=I3tS2oTUvHI&list=RDDvIauQX0NvE&index=6")
                
                elif "internet speed" in query:
                    wifi = speedtest.Speedtest()
                    upload_speed = wifi.upload()/1048576
                    download_speed = wifi.download()/1048576
                    print("The upload speed is", upload_speed)
                    print("the download speed is", download_speed)
                    speak(f"Wifi upload speed is{upload_speed}")
                    speak(f"Wifi download speed is{download_speed}")

                elif "screenshot" in query:
                    im = pyautogui.screenshot()
                    im.save("ss.jpg")

                elif "click my photo" in query:
                    pyautogui.press("super")
                    pyautogui.typewrite("camera")
                    pyautogui.press("enter")
                    pyautogui.sleep(2)
                    speak("SMILE")
                    pyautogui.press("enter")

                elif "translate" in query:
                    from translate import translategl
                    query = query = query.replace("coco", "")
                    query = query = query.replace("translate", "")
                    translategl(query)

                elif "shutdown the system" in query:
                    speak("Are you sure you want to shutdown the system?")
                    shutdown = input("Do you wish to shut down?(yes/no)")
                    if shutdown == "yes":
                        os.system("shutdown /s /t 1")
                    elif shutdown == "no":
                        break

                #elif "finally sleep" in query:
                # speak("going to sleep, sir")
                # exit()

            
