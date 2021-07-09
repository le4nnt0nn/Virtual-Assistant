import pyttsx3

# - este método permite que la máquina hable
def talk(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()