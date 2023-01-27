import random

def Respuestas(número):
    if número == 1:
        return 'Veo certero el camino'
    elif número == 2:
        return 'Decididamente sí'
    elif número == 3:
        return 'SÍ'
    elif número == 4:
        return 'Mi respuesta es SÍ, AHRE'
    elif número == 5:
        return 'Volvé a preguntar más tarde'
    elif número == 6:
        return 'Estás descontcentradx, volvé a preguntar'
    elif número == 7:
        return 'Mi respuesta es NO, AHRE'
    elif número == 8:
        return 'No'
    elif número == 9:
        return 'Muy dudoso'

def NuevoJuego():
    print('Piensa en una pregunta sí/no, y pulsa enter para ver la respuesta')
    input()

def JugarDeNuevo():
    JuegoNuevo=input('Quieres hacer una nueva pregunta? y/n')
    if JuegoNuevo=='y' or JuegoNuevo=='Y':
        NuevoJuego()
        print(Respuestas(random.randint(1,9)))
        JugarDeNuevo()

    else:
        print('Adiós, que la fuerza te acompañe! AHRE')
        quit()

       


#programa principal
NuevoJuego()
print(Respuestas(random.randint(1,9)))
JugarDeNuevo()