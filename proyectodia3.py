texto = 'En el vasto mundo de la programación, Python es uno de los lenguajes más populares. Es conocido por su simplicidad y legibilidad, lo que lo hace ideal para principiantes y expertos por igual. Python se utiliza en diversas áreas, desde el desarrollo web hasta el análisis de datos y la inteligencia artificial. Es un lenguaje versátil y poderoso que ha ganado una gran comunidad de usuarios en todo el mundo. Por su flexibilidad y facilidad de uso, Python ha sido adoptado por muchas empresas y organizaciones. Además, la comunidad de Python ofrece numerosos recursos para aprender y mejorar continuamente.'
texto_formateado = texto.lower()

letras_seleccionadas = []
letras_seleccionadas.append(input('escribe una letra: ').lower())
letras_seleccionadas.append(input('escribe una letra: ').lower())
letras_seleccionadas.append(input('escribe una letra: ').lower())

print(f'la letra {letras_seleccionadas[0]} aparece', texto_formateado.count(letras_seleccionadas[0]))
print(f'la letra {letras_seleccionadas[1]} aparece', texto_formateado.count(letras_seleccionadas[1]))
print(f'la letra {letras_seleccionadas[2]} aparece', texto_formateado.count(letras_seleccionadas[2]))

lista_palabras = texto.split()

print(f'hay un total de {len(lista_palabras)} palabras')
print(f'La primer letra es {texto[0]} y la ultima {texto[-1]}')

text_invertido = texto_formateado[::-1]
print(f'invertido el texto quedaria asi: {text_invertido}')

pitoncondicion = "python" in texto_formateado
print(f'La palabra Python se encuentra en sistema? {pitoncondicion}')
      