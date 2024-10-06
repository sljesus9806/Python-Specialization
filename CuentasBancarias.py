import sys
import os
import time

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f'Nombre: {self.nombre}, Edad: {self.edad}'
    
    
    
    

class Cliente(Persona):
    def __init__(self, nombre, edad, numero_cuenta, saldo):
        super().__init__(nombre, edad)
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo
    
    def __str__(self):
        return f'Nombre: {self.nombre}, Edad: {self.edad}, Numero de cuenta: {self.numero_cuenta}, Saldo: {self.saldo}'
        

    def depositar(self, cantidad):
        self.saldo += cantidad
        return f'Su saldo actual es de: {self.saldo}'
    
    def retirar(self, cantidad):
        if cantidad > self.saldo:
            return 'Saldo insuficiente'
        self.saldo -= cantidad
        return f'Su saldo actual es de: {self.saldo}'
    


while True:
    print('1. Crear cuenta')
    print('2. Depositar')
    print('3. Retirar')
    print('4. Consultar cuenta')
    print('5. Salir')
    opcion = int(input('Opcion: '))

    match opcion:
        case 1:
            nombre = input('Nombre: ')
            edad = int(input('Edad: '))
            numero_cuenta = input('Numero de cuenta: ')
            saldo = float(input('Saldo: '))
            cliente_usr = Cliente(nombre, edad, numero_cuenta, saldo)
            print(cliente_usr)
            time.sleep(4)
            clear()
        case 2:
            cliente_usr.depositar(float(input('Cantidad a depositar: ')))
            print(cliente_usr)
            time.sleep(4)
            clear()
        case 3:
            cliente_usr.retirar(float(input('Cantidad a retirar: ')))
            print(cliente_usr)
            time.sleep(4)
            clear()
        case 4:
           try:
               print(cliente_usr)
               time.sleep(4)
               clear()
           except NameError:
                print('Primero cree una cuenta')
        case 5:
            break
            



