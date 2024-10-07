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

'''class Padre:
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
    
'''

'''class Vaca:
    
    def __init__(self, nombre):
        self.nombre = nombre
        
    def hablar(self):
        print(self.nombre, "dice muuu")

class Oveja:
    
    def __init__(self, nombre):
        self.nombre = nombre
        
    def hablar(self):
        print(self.nombre, "dice beee")     '''


'''palabra = "polimorfismo"
lista = ['Clases', 'POO', 'Polimorfismo']
tupla = (1, 2, 3, 4, 5)

#create an iterator that runs over the objects and print len of each object

def len_iterador(*args):
    for objeto in args:
        print(len(objeto))

len_iterador(palabra, lista, tupla)
'''


'''class Mago():
    def atacar(self):
        print("Ataque mágico")

class Arquero():
    def atacar(self):
        print("Lanzamiento de flecha")

class Samurai():
    def atacar(self):
        print("Ataque con katana")
        

def ataque(heroe):
    heroe.atacar()

mago = Mago()
arquero = Arquero()
samurai = Samurai()

iterable = [mago, arquero, samurai]

for heroe in iterable:
    ataque(heroe)'''
    
'''     
class Mago():
    def defender(self):
        print("Escudo mágico")

class Arquero():
    def defender(self):
        print("Esconderse")

class Samurai():
    def defender(self):
        print("Bloqueo")
        
        
def personaje_defender(heroe):
     heroe.defender()
     '''

'''class CD:
    def __init__(self, autor, titulo, canciones): 
        self.autor = autor
        self.titulo = titulo
        self.canciones = canciones
    def __str__(self):
        return f'album: {self.titulo} de {self.autor} con {self.canciones} canciones'
    
    def __len__(self):
        return self.canciones
    
        
        
                
mi_cd = CD("Queen", "Greatest Hits", 24)

print(mi_cd)
print(len(mi_cd))'''
