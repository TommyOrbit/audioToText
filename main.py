import speech_recognition as sr
import os
import glob

file_dir = './'
extension_list = ("*.wav", " ")

def speech_to_text():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
    try:
        print("You said: " + r.recognize_google(audio, language='zh-tw'))
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

def audio_to_text(dir):
    r = sr.Recognizer()
    os.chdir(dir)
    for extension in extension_list:
        for file in glob.glob(extension):
            with sr.AudioFile(file) as source:
                audio = r.record(source)
            try:
                print("{filename}: \n{text}\n\n".format(filename=file, text=r.recognize_google(audio, language='zh-tw')))
            except sr.UnknownValueError:
                print("Could not understand audio")
            except sr.RequestError as e:
                print("Could not request results; {0}".format(e))


audio_to_text(file_dir)
