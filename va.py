import speech_recognition as  sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyowm
import random
from wikipedia.wikipedia import random

# - puedes cambiar el nombre al que quieras
name = "alexa"


# - escuchador y motor 
listener = sr.Recognizer()
engine = pyttsx3.init()

# - weather
owm = pyowm.OWM('649596c70acbd15c65ae8da5b1bf5ab2')
# - puedes cambiar el nombre de la ciudad para obtener sus datos del tiempo
city = "Seville"
loc = owm.weather_at_place(city)
weather = loc.get_weather()
# - temperatura
temp = weather.get_temperature(unit="celsius")

#- selecciono el valor de la key de temperatura
for key,val in temp.items():
    if key=="temp":
        tempi = {val} 

# - tiempo
loc = owm.three_hours_forecast(city)
# - pregunta si habrá nubes o lluvia en tu ciudad
clouds = str(loc.will_have_clouds())
rain = str(loc.will_have_rain())



# - este método permite que la máquina repita lo que tu digas
def talk(text):
    engine.say(text)
    engine.runAndWait()

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

# - run arranca el asistente
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
    elif "temperatura" in rec:
        talk("Ahora mismo en tu ciudad hacen "+str(tempi)+" grados celsius")
        # - te dice la temperatura que hay en tu ciudad
    elif "lluvia"  in rec:
        if rain==True:
            talk("Si, se espera lluvia en el día de hoy")
        else:
            talk("No, hoy no se espera lluvia")
        # - chequea si va a llover o no
    elif "nublado" in rec:
        if clouds==True:
            talk("Si, hoy se espera un dia nublado")
        else:
            talk("No, hoy el cielo va a estar totalmente despejado")
        # - chequea si va a estar nublado o no
    elif "me quieres" or "me amas" or "me adoras" in rec:
        rand = random.randint(0,3)
        if rand==0:
            talk("Ya estoy comprometida con la calculadora de tu pc, lo siento")
        elif rand==1:
            talk("Creo que será mejor que te busques una pareja de tu especie, gracias")
        elif rand==2:
            talk("Si, pero como amigos")
        elif rand==3:
            talk("Qué asco, no digas esas cosas")
    else:
        talk("No te he entendido, vuelve a intentarlo")

while True:
    run()