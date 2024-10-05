import os
import pathlib  

#learning directories management and files

print("Current directory: ", os.getcwd())

print('Tyoe a name for a new directory: ')
new_dir = input()
os.mkdir(new_dir)

