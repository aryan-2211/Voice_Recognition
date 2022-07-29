import speech_recognition
import pyttsx3
import pywhatkit
import webbrowser
import wikipedia

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source, 0, 4)

    try:
        print("Understanding...")
        query = r.recognize_google(audio, language = 'en-in')
        print(f"You said : {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query

query = takeCommand().lower()

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate", 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def searchGoogle(query):
    if "google" in query:
        import wikipedia as googleScrap
        query = query.replace("coco", "")
        query = query.replace("google", "")
        query = query.replace("google search", "")
        speak("this is what I found on google")

        try:
            pywhatkit.search(query)
            result = googleScrap.summary(query, 2)
            print(result)
            speak(result)
        except:
            speak("No speakable output available")

def searchYT(query):
    if "youtube" in query:
        speak("This is what I found!")
        query = query.replace("youtube search", "")
        query = query.replace("youtube", "")
        query = query.replace("coco", "")
        web = "https://www.youtube.com/results?search_query=" + query
        webbrowser.open(web)
        pywhatkit.playonyt(query)
        speak("Done, Sir")
