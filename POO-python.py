#Lets learn about Object Oriented Programming in Python
#----------------------------------------------
#Object Oriented Programming (OOP) is a programming paradigm that uses objects to represent data and methods to manipulate that data.
#In OOP, objects are instances of classes.
#Classes define the properties and behavior of objects.
#Objects are instances of classes.
#Objects have attributes and methods.
#Attributes are variables that store data.
#Methods are functions that operate on the data.
#----------------------------------------------

class Padre:
    def trabajar(self):
        print("Trabajando en hospital")
    def reir(self):
        print("Jajajaja")

class Madre():
    def trabajar(self):
        print("Trabajando en casa")
        
class Hijo(Padre, Madre):
    def reir(self):
        return super().reir()
    def trabajar(self):
        return super().trabajar()
    
    
diego = Hijo()
diego.trabajar()
diego.reir()
    

