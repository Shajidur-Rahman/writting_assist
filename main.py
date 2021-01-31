import speech_recognition as sr
from text_to_speech import speak 
r = sr.Recognizer()
while True:
    with sr.Microphone() as mic:
        print("listening")
        text = r.listen(mic)
        try:
            reco = r.recognize_google(text)
            print(reco)
        except sr.UnknownValueError:
            print("please speak again")
            speak("please speak again", lang="en", save=True, file="hello.mp3")
        except sr.RequestError as p:
           speak("hello", lang="en", save=True, file="hello.mp3")
