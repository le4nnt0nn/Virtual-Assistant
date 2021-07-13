from io import open

def reminder(frase):
    file = open("reminder.txt","w")
    file.write(frase)
    file.close()
# - crea un archivo de texto