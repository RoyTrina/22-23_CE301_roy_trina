import speech_recognition

class VoiceDetector:
    recognizer = speech_recognition.Recognizer()

    with speech_recognition.Microphone() as source:
        print("Speak now...")
        sound = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(sound)
        print("")
    except speech_recognition.UnknownValueError:
        print("")
    except speech_recognition.RequestError as exception:
        print("")
