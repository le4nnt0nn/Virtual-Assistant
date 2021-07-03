import speech_recognition as  sr
import pyttsx3

# - puedes cambiar el nombre al que quieras
name = "cuca"
listener = sr.Recognizer()

engine = pyttsx3.init()

# - este método permite que la máquina repita lo que tu digas
def talk(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    try:
        with sr.Microphone() as source:
            print("Escuchando...")
            voice = listener.listen(source)
            rec = listener.recognize_google(voice)
            rec = rec.lower()
            # - si el nombre seleccionado se escucha, lo repite
            if name in rec:
                rec = rec.replace(name, '')
                print(rec)
            # talk(rec) - repite lo que dices    
            # print(rec) - imprime lo que dices
    except:
        pass
    # - retorna rec
    return rec

def run():
    # - rec recoge el valor de listen
    rec = listen()
    if 'reproduce' in rec:
        music = rec.replace("reproduce", "")
        talk("Reproduciendo "+ music)


run()