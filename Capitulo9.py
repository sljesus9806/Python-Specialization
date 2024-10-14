mi_archivo = open('texto.txt')

lineas = archivo.readlines()
print(lineas[1])

mi_archivo.close()



#------------------------------------------------------------

#aperture modes
#open(filename, mode)
#r: read
#w: write
#a: append
#r+: read and write
#w+: write and read
#a+: append and read
#x: exclusive creation


archivo = open('texto.txt', 'w')
archivo.write('Hola mundo')
archivo.close()
