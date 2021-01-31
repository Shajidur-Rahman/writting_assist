import speech_recognition as sr
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
        except sr.RequestError as p:
            print('')
          
