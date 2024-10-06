import os
from pathlib import Path
#learning directories management and files

'''print("Current directory: ", os.getcwd())

print('Type a name for a new directory: ')
new_dir = input()
os.mkdir(new_dir)
'''
#----------------------------------------------


carpeta = Path("../Python-Specialization")
archivo = carpeta / "archivo.txt"
mi_archivo = open(archivo)
print(mi_archivo.read())


#----------------------------------------------

#whats pathlib?
#The pathlib module was introduced in Python 3.4, and it provides classes for working with the file system.
#These classes are actually objects that represent file paths.
#The Path class is the primary class in the pathlib module.
#It is used to represent file or directory paths.
#The Path class has a number of methods that allow you to manipulate file paths.
#The Path class is used to create a Path object, which represents a file or directory path.
#The Path object has a number of methods that allow you to manipulate the path.



#----------------------------------------------
#The Path class has a number of methods that allow you to manipulate file paths.
#Some of the most commonly used methods are:

