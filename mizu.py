import speech_recognition as  sr
import pyttsx3

# - puedes cambiar el nombre al que quieras
name = "ruka"
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
        rec = rec.lower()
        # - si el nombre seleccionado se escucha, lo repite
        if name in rec:
            talk(rec)
        # print(rec) - imprime lo que dices
except:
    pass