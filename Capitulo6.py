fname = 'romeo.txt'
fh = open(fname,'r')
content = fh.read()
fh.close()
correo = 0
count = 0
x = 0

# Separar el texto en palabras
palabras = content.split()

# Lista para almacenar los correos electrónicos encontrados
correos_encontrados = []

for palabra in palabras:
    if palabra.lower() == "from":
        correo = palabras[x + 1] 
        if "@" in correo:
            correos_encontrados.append(correo)
    
    x += 1
  


for n in correos_encontrados:
    print(n)
    count += 1

print("There were", count, "lines in the file with From as the first word")
