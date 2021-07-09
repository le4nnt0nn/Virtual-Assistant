from .talk import talk

def love(rand):
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