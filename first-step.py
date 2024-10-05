import os
from pathlib import Path
#learning directories management and files

'''print("Current directory: ", os.getcwd())

print('Tyoe a name for a new directory: ')
new_dir = input()
os.mkdir(new_dir)
'''
#----------------------------------------------


carpeta = Path("../Python-Specialization")
archivo = carpeta / "archivo.txt"
mi_archivo = open(archivo)
print(mi_archivo.read())