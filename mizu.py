import speech_recognition as  sr
import pyttsx3

listener = sr.Recognizer()

engine = pyttsx3.init()

# - este método permite que la máquina repita lo que tu digas
def talk(text):
    engine.say(text)
    engine.runAndWait()


try:
    with sr.Microphone() as source:
        print("Escuchando...")
        voice = listener.listen(source)
        rec = listener.recognize_google(voice)
        talk(rec)
        # print(rec) - imprime lo que dices
except:
    pass