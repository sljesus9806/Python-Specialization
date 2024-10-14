from random import *


"""numero = 50

while numero != -1:
    if numero%5 == 0:
        print(numero)
    numero -= 1"""
    
"""lista_numeros = [4,5,8,7,6,9,8,2,4,5,7,1,9,5,6,-1,-5,6,-6,-4,-3]

for numero in lista_numeros:
    if numero < 0:
        break
    else:
        print(numero)
        """


"""mi_lista = list(range(3,301,3))
print(mi_lista)
        """

"""suma_cuadrados = list(range(1,16))
suma = 0

for numero in suma_cuadrados:
    cuadrado = numero**2
    suma = suma + cuadrado
suma_cuadrados = suma
print(suma_cuadrados)"""

"""def area(lado,base):
    
    area_total = lado * base
    return area_total"""
    
"""def calcular_promedio():
    promedios = []
    x = "si"
    #formula de promedio
    while x == "si":
        promedios.append(float(input('Ingrese promedio: ')))
        x = input('desea ingresar otro promedio? si/no:  ')
    if len(promedios) == 0:
        return 'Papi estas pendejo? no ingresaste ni madres'
    promedio = sum(promedios) / len(promedios)  
    return promedio    



lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

for ind,nombre in enumerate(lista_nombres):
    if nombre.startswith("M"):
        print(ind)

"""
        
diccionario_edades = {"Carlos":55, "María":42, "Mabel":78, "José":44, "Lucas":24, "Rocío":35, "Sebastián":19, "Catalina":2,"Darío":49}

edad_minima = min(diccionario_edades.values())
ultimo_nombre = max(diccionario_edades)        