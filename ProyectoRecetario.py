from os import system, name
from pathlib import Path
import time


#directories
directorio_Carnes = Path("./Carnes")
directorio_Pastas = Path("./Pastas")
directorio_Ensaladas = Path("./Ensaladas")
directorio_Postres = Path("./Postres")


#validate OS type
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

#definir funciones

def leer_recetas(nombre_receta):
    ruta  = Path(directorio_Carnes/nombre_receta / ".txt")
    if ruta.exists():
        print('Receta encontrada: \n')
        print(ruta.read_text())
        time.sleep(4)
        clear()
    elif (ruta := Path(directorio_Pastas/nombre_receta / ".txt")).exists():
        print('Receta encontrada: \n')
        print(ruta.read_text())  
        time.sleep(4)  
        clear()
    elif (ruta := Path(directorio_Ensaladas/nombre_receta / ".txt")).exists():
        print('Receta encontrada: \n')
        print(ruta.read_text())
        time.sleep(4)
        clear()
    elif (ruta := Path(directorio_Postres/nombre_receta / ".txt")).exists():
        print('Receta encontrada: \n')
        print(ruta.read_text())
        time.sleep(4)
        clear()
    else:
        print('Receta no encontrada')
        time.sleep(4)
        clear()
        
        
def crear_receta(nombre_receta):
    print('Cuantos ingredientes tiene la receta?')
    cantidad_ingredientes = int(input())
    ingredientes = []
    for i in range(cantidad_ingredientes):
        print(f'Ingrese el ingrediente {i+1}')
        ingredientes.append(input())
    receta_pasos = []
    while True:
        print('Ingrese un paso para la receta o escriba "fin" para terminar')
        paso = input()
        if paso == 'fin':
            break
        receta_pasos.append(paso)
    print('Ingrese la categoria de la receta:  Carnes,  Pastas,  Ensaladas,  Postres')
    categoria = input().capitalize()
    
    #determine directory
    directorios = {
        'Carnes': directorio_Carnes,
        'Pastas': directorio_Pastas,
        'Ensaladas': directorio_Ensaladas,
        'Postres': directorio_Postres
    }
    
    if categoria not in directorios:
        print('Categoria no válida')
        return
        
    
    #File creation
    
    ruta = directorios[categoria] / f'{nombre_receta}.txt'
    
    #write the recipe
    with open(ruta, 'w') as archivo:
        archivo.write('Ingredientes:\n')
        for ingrediente in ingredientes:
            archivo.write(f'- {ingrediente}\n')
        archivo.write('\nPasos:\n')
        for i, paso in enumerate(receta_pasos):
            archivo.write(f'{i+1}. {paso}\n')
    print('Receta creada')
    time.sleep(4)
    clear()
    
    
def crear_categoria(nombre_categoria):
    directorio = Path(f'./{nombre_categoria}')
    if directorio.exists():
        print('La categoria ya existe')
        time.sleep(4)
        clear()
        return
    directorio.mkdir()
    print('Categoria creada')
    time.sleep(4)
    clear()

def eliminar_receta(nombre_receta):
    ruta = Path(directorio_Carnes/nombre_receta / ".txt")
    if ruta.exists():
        ruta.unlink()
        print('Receta eliminada')
        time.sleep(4)
        clear()
        return
    ruta = Path(directorio_Pastas/nombre_receta / ".txt")
    if ruta.exists():
        ruta.unlink()
        print('Receta eliminada')
        time.sleep(4)
        clear()
        return
    ruta = Path(directorio_Ensaladas/nombre_receta / ".txt")
    if ruta.exists():
        ruta.unlink()
        print('Receta eliminada')
        time.sleep(4)
        clear()
        return
    ruta = Path(directorio_Postres/nombre_receta / ".txt")
    if ruta.exists():
        ruta.unlink()
        print('Receta eliminada')
        time.sleep(4)
        clear()
        return
    print('Receta no encontrada')
    time.sleep(4)
    clear()    
    

def eliminar_categoria(nombre_categoria):
    directorio = Path(f'./{nombre_categoria}')
    if directorio.exists():
        directorio.rmdir()
        print('Categoria eliminada')
        time.sleep(4)
        clear()
        return
    print('Categoria no encontrada')
    time.sleep(4)
    clear()


#Bienvenida al Recetario de Cocina

while True:
    print("Bienvenido al Recetario de Cocina")
    print('''Este programa te permitirá buscar recetas de cocina, agregar nuevas recetas y guardarlas en un archivo de texto
para que puedas consultarlas en cualquier momento.

[1] - Leer recetas
[2] - Crear receta
[3] - Crear categoria
[4] - Eliminar receta
[5] - Eliminar categoria
[6] - Salir
''')
    opcion = input("Seleccione una opción: ")
    clear()
    match opcion:
        case "1":
            print("Ingrese el nombre de la receta que desea buscar: ")
            nombre_receta = input()
            leer_recetas(nombre_receta)
            continue
        case "2":
            print("Ingrese el nombre de la receta que desea crear: ")
            nombre_receta = input()
            crear_receta(nombre_receta)
            continue
        case "3":
            print("Ingrese el nombre de la categoria que desea crear: ")
            nombre_categoria = input()
            crear_categoria(nombre_categoria)
            continue
        case "4":
            print("Ingrese el nombre de la receta que desea eliminar: ")
            nombre_receta = input()
            eliminar_receta(nombre_receta)
            continue
        case "5":
            print("Ingrese el nombre de la categoria que desea eliminar: ")
            nombre_categoria = input()
            eliminar_categoria(nombre_categoria)
            continue
        case "6":
            print("Gracias por usar el Recetario de Cocina")
            break
        case _:
            print("Opción no válida, por favor intente de nuevo")
            continue

#----------------------------------------------