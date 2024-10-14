
#------------------------------------------------------------
lista_numeros = [1, 2, 3, 25, 3]

def reducir_lista(lista):
    for n in lista:
        conteo = lista.count(n)
        indice = lista.index(n)
        if conteo > 1:
            lista.pop(indice)
    valor_max = max(lista)
    lista_final = lista.remove(valor_max)   
    return lista_final

def promedio(lista_num):
    return sum(lista_num) / len(lista_num)        


#Or this is other way to do it

lista_numeros = [1,2,15,7,2,8]
 
def reducir_lista2(lista):
    lista = list(set(lista))
    lista.sort()
    lista.pop(-1)
    return lista
 
def promedio2(lista):
    valor_medio = sum(lista)/len(lista)
    return valor_medio

if __name__ == '__main__':
    reducir_lista(lista_numeros)
    print(promedio(lista_numeros))
    
    reducir_lista2(lista_numeros)
    print(promedio2(lista_numeros)) 
    
    
#------------------------------------------------------------
import random
lista_numeros = [1, 2, 3, 4, 5]
def lanzar_moneda():
    return random.choice(['C    ara', 'Cruz'])
def probar_suerte(resultado, lista_numeros):
    if resultado == 'Cara':
        print('la lista se autodestruira')
        lista_numeros.clear()
    else:
        print('la lista se salvara')
    return lista_numeros

#------------------------------------------------------------
#now lets go to arguments defined *args and **kwargs
#whats *args? *args is a way to pass a variable number of arguments to a function
#it is used to pass a non-keyworded, variable-length argument list
#it is used to pass a variable number of non-keyworded arguments to a function
#The syntax is to use the symbol * to take in a variable number of arguments; by convention, it is often used with the word args

def suma(*args):
    return sum(args)



#------------------------------------------------------------

def suma_cuadrados(*args):
    return sum([n**2 for n in args])
print(suma_cuadrados(1,2,3))

def suma_absolutos(*args):
    return sum([abs(n) for n in args])

def numeros_persona(nombre,*args):
    
    return f'{nombre}, la suma de tus números es {sum(args)}'

#------------------------------------------------------------
#**kwargs is used to pass a keyworded, variable-length argument list
#**kwargs is used to pass a keyworded, variable-length argument list to a function
#The syntax is to use the double asterisk ** before the parameter name to denote this type of argument
#The arguments are passed as a dictionary and these arguments make a dictionary inside function with name same as the parameter excluding double asterisk **
#**kwargs allows you to pass keyworded variable length of arguments to a function

def suma(**kwargs):
    
    return sum(kwargs.values())

print(suma(a=1, b=2, c=3))


def cantidad_de_atributos(**kwargs):
    return len(kwargs)

def lista_atributos(**kwargs):
    return list(kwargs.values())

def describir_persona(nombre, **kwargs):
    print(f'Características de {nombre}')
    for key, value in kwargs.items():
        print(f'{key}: {value}')
        

#------------------------------------------------------------

def devolver_distintos(*args):
    if sum(args) > 15:
        return max(args)
    elif sum(args) < 10:
        return min(args)
    elif sum(args) >= 10 and sum(args) <= 15:
        valor_intermedio = sum(args) / len(args)
        return valor_intermedio
    
def unique_leters(word): #this function will return the unique letters of a word and sort them
    return sorted(set(word))

def valuate_zero(*args):
    conteo = 0
    for n in args:
        if n == 0:
           conteo += 1
           if conteo == 2:
               conteo = 0
               return True
           else:
               continue
           
def contar_primos(*args):
    conteo = 0
    for n in args:
        if n > 1:
            for i in range(2, n):
                if n % i == 0:
                    break
            else:
                conteo += 1
    return conteo