# - imports propios
import sys
from functions.talk import talk
from functions.listen import listen
from functions.jokes import jokes
from functions.love import love
from functions.calendar import calendar, goCalendar

# - otras librerías
import pywhatkit
import datetime
import wikipedia
import pyowm
import random


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
    elif "me quieres" in rec:
        # - random for choices
        rand = random.randint(0,3)
        love(rand)
        # - genera respuestas aleatorias sobre amor
    elif "chiste" in rec:
        # - random for choices
        rand = random.randint(0,3)
        jokes(rand)
        # - genera chistes aleatorios
    elif "calendario" in rec:
        talk("Mostrando el calendario")
        goCalendar()
        # - muestra el calendario
    elif "gracias" in rec:
        talk("De nada, espero haberte ayudado")
        sys.exit(0)
        # - Sale del programa
while True:
    run()