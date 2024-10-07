import os
import time

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

#Turnos Generated
Turnos_Cosmeticos = []
Turnos_Medicamentos = []
Turnos_Perfumeria = []

#Globals for count of turns
Turnos_Cosmeticos_Count = 0
Turnos_Medicamentos_Count = 0
Turnos_Perfumeria_Count = 0

#Function to generate turns
def generar_turno(Opcion):
    if Opcion == 1:
        global Turnos_Cosmeticos_Count
        Turnos_Cosmeticos_Count += 1
        Turnos_Cosmeticos.append(Turnos_Cosmeticos_Count)
        print(f"Turno Cosmeticos c-{Turnos_Cosmeticos_Count}")
    elif Opcion == 2:
        global Turnos_Medicamentos_Count
        Turnos_Medicamentos_Count += 1
        Turnos_Medicamentos.append(Turnos_Medicamentos_Count)
        print(f"Turno Medicamentos m-{Turnos_Medicamentos_Count}")
    elif Opcion == 3:
        global Turnos_Perfumeria_Count
        Turnos_Perfumeria_Count += 1
        Turnos_Perfumeria.append(Turnos_Perfumeria_Count)
        print(f"Turno Perfumeria p-{Turnos_Perfumeria_Count}")
    else:
        print("Opcion no valida")

        
while True:
    clear()
    print("Bienvenido a Farmacia la joya")
    print("#"*30)
    print("Seleccione una opcion")
    print(''' [1] Cosmeticos, [2] Medicamentos, [3] Perfumeria, [4] Salir''')   
    try:
        opcion = int(input("Ingrese una opcion: "))
    except ValueError:
        print("Opcion no valida Ingresa un numero")
        continue
    match opcion:
        case 1:
            clear()
            generar_turno(opcion)
            time.sleep(2)
        case 2:
            clear()
            generar_turno(opcion)
            time.sleep(2)
        case 3:
            clear()
            generar_turno(opcion)
            time.sleep(2)
        case 4:
            print("Gracias por visitarnos")
            break
    
        
        
