from random import *
numero_random = randint(1, 100)
intentos = 0


print('Presentate: \n')
nombre = input()
print('Hola, ' + nombre + '!\n')


print('Adivina el número que estoy pensando entre 1 y 100: \n')
print('solo tienes 8 intentos\n')


while intentos < 8:
    intento = input('Intento: ')
    intento = int(intento)
    intentos = intentos + 1
    match (intento < numero_random, intento > numero_random, intento == numero_random, intento > 100, intento < 1, intentos == 8):
        case (True, False, False, False, False, False):
            print('tu número es muy bajo, intenta de nuevo\n')
            continue
        case (False, True, False, False, False, False):
            print('tu número es muy alto, intenta de nuevo\n')
            continue
        case (False, False, True, False, False, False):
            print('Felicidades, ' + nombre + '! Adivinaste el número en ' + str(intentos) + ' intentos\n')
            break
        case (False, False, False, True, False, False):
            print('tu número está fuera de rango, intenta de nuevo\n')
            continue
        case (False, False, False, False, True, False):
            print('tu número está fuera de rango, intenta de nuevo\n')
            continue
        case (False, False, False, False, False, True):
            print('Lo siento, ' + nombre + ', no adivinaste el número. El número era ' + str(numero_random) + '\n')
            break
        
print('Fin del juego\n')