import speech_recognition as  sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia

# - puedes cambiar el nombre al que quieras
name = "alexa"
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
            rec = listener.recognize_google(voice, language='es-ES')
            rec = rec.lower()
            # - si el nombre seleccionado se escucha, lo repite
            if name in rec:
                # - replace evita que diga su nombre en la rec
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
        # playonyt permite reproducir la musica en youtube
        pywhatkit.playonyt(music)
    elif "hora" in rec:
        hora = datetime.datetime.now().strftime('%I:%M %p')
        talk("Son las "+hora)
        # permite devolver la hora
    elif "busca" in rec:
        order = rec.replace("busca", "")
        info = wikipedia.summary(order, 1)
        talk(info)
        # permite buscar cualquier cosa en wikipedia
    else:
        talk("No te he entendido, vuelve a intentarlo")

while True:
    run()