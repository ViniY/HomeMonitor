import speech_recognition as sr
import text_to_speech as speech



r = sr.Recognizer()
def listening():
    with sr.Microphone() as src:
        print("I'm listening")
        speech.speak(" I am listening")
        audio = r.listen(src)

    # recognize speech using Google Speech Recognition
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        heardText = r.recognize_google(audio)
        print("Google Speech Recognition thinks you said " + heardText)
        return heardText
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
