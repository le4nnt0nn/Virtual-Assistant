import speech_recognition as  sr
# - escuchador y motor 
listener = sr.Recognizer()

# - puedes cambiar el nombre al que quieras
name = "alexa"


# - método que permite escuchar desde tu micrófono
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