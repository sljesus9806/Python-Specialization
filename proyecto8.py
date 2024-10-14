#vamos a programar el juego del ahorcado

from random import *


turnos = 0
vidas = 6
secret_words = ['casa', 'perro', 'gato', 'computadora', 'celular', 'teclado', 'raton', 'monitor', 'ventana', 'puerta']
correctas = []
               
secret_word = choice(secret_words)
lenght_word = len(secret_word)
estado_actual = ['_'] * lenght_word  # Estado inicial de la palabra secreta con guiones bajos


def pedir_letra():
    letra = input('Dame una letra: ')
    return letra

def eliminar_turno():
    global turnos
    turnos += 1
    return turnos

def eliminar_vida():
    global vidas
    vidas -= 1
    return vidas

def evaluacion_letra(letra):
    global secret_word
    letra_encontrada = False  # Variable para saber si la letra se encuentra
    for index, char in enumerate(secret_word):  # Recorre la palabra secreta con su índice
        if char == letra:  # Evalúa si la letra está en la palabra secreta
            estado_actual[index] = char  # Actualiza el estado actual
            letra_encontrada = True
    return letra_encontrada  # Devuelve True si la letra está, False si no


if __name__ == '__main__':
    print('Bienvenido al juego del ahorcado')
    print('La palabra secreta tiene', lenght_word, 'letras')
    
    
    while vidas > 0:
        print(' '.join(estado_actual)) # Imprime el estado actual de la palabra secreta
        print('Tienes', vidas, 'vidas')
        
        letra = pedir_letra()
        if evaluacion_letra(letra) == True:
            print('La letra', letra, 'se encuentra en la palabra secreta')
            print('Tienes', vidas, 'vidas')
            correctas.append(letra)
        else:
            print('La letra', letra, 'no se encuentra en la palabra secreta')
            eliminar_vida()
        if '_' not in estado_actual:
            print('felicidades, ganaste!')   
            break
    
    if vidas == 0:
        print('Perdiste, la palabra secreta era:', secret_word)


