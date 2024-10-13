import pygame
import random
import math

# Inicializar pygame
pygame.init()
se_ejecuta = True

# Configuración de la ventana
pantalla = pygame.display.set_mode((1024, 768))
pygame.display.set_caption('Invasión Espacial')
icono = pygame.image.load('ovn.png')
pygame.display.set_icon(icono)

# Jugador
img_jugador = pygame.image.load('nave-espacial.png')
jugador_x = 480
jugador_y = 768 - 64
jugador_x_cambio = 0  # Velocidad del jugador

# Función para dibujar el jugador en pantalla
def jugador_pos(x, y):
    pantalla.blit(img_jugador, (x, y))

# Función para dibujar al enemigo
def enemigo(x, y, i):
    pantalla.blit(img_mar[i], (x, y))

# Función para disparar el misil
def disparo(x, y):
    global misil_estado
    misil_estado = True
    pantalla.blit(img_misil, (x + 16, y + 10))  # Alinear misil con el centro de la nave

# Función para detectar colisiones entre el misil y el enemigo
def hay_colision(mar_x, mar_y, misil_x, misil_y):
    distancia = math.sqrt(math.pow(mar_x - misil_x, 2) + math.pow(mar_y - misil_y, 2))
    if distancia < 27:  # Ajustar el valor según el tamaño de tus sprites
        return True
    else:
        return False

# Imagen de fondo
fondo = pygame.image.load('fondo.jpg')

# Variables del misil
img_misil = pygame.image.load('misil.png')
misil_x = 0
misil_y = jugador_y  # Iniciar desde la posición del jugador
misil_y_cambio = 1  # Velocidad del misil
misil_estado = False  # El misil no ha sido disparado

# ----------- Múltiples enemigos -----------
# Cargar la imagen del enemigo
img_mar = []
mar_x = []
mar_y = []
mar_x_cambio = []
mar_y_cambio = []
num_enemigos = 5  # Número de enemigos

# Inicializar varios enemigos
for i in range(num_enemigos):
    img_mar.append(pygame.image.load('dracu.png'))  # Imagen del enemigo
    mar_x.append(random.randint(0, 960))  # Posición inicial X aleatoria
    mar_y.append(random.randint(50, 150))  # Posición inicial Y aleatoria
    mar_x_cambio.append(0.3)  # Velocidad de movimiento en X
    mar_y_cambio.append(40)  # Desplazamiento en Y cuando toca los bordes

# Bucle principal del juego
while se_ejecuta:
    pantalla.blit(fondo, (0, 0))

    # Detectar teclas presionadas
    teclas = pygame.key.get_pressed()

    # Movimiento del jugador
    if teclas[pygame.K_LEFT] or teclas[pygame.K_a]:
        jugador_x -= 0.3
    if teclas[pygame.K_RIGHT] or teclas[pygame.K_d]:
        jugador_x += 0.3

    # Limitar el movimiento del jugador dentro de la pantalla
    if jugador_x <= 0:
        jugador_x = 0
    elif jugador_x >= 960:
        jugador_x = 960

    # Disparo del misil
    if teclas[pygame.K_SPACE]:
        if not misil_estado:  # Solo disparamos si el misil no está ya en movimiento
            misil_x = jugador_x  # El misil debe dispararse desde la posición del jugador
            misil_y = jugador_y  # Posición inicial del misil es la posición del jugador
            disparo(misil_x, misil_y)

    # Movimiento del misil cuando se ha disparado
    if misil_estado:
        disparo(misil_x, misil_y)
        misil_y -= misil_y_cambio  # El misil se mueve hacia arriba

        # Restablecer el misil si sale de la pantalla
        if misil_y <= 0:
            misil_y = jugador_y
            misil_estado = False  # El misil está listo para ser disparado de nuevo

    # Movimiento de los enemigos
    for i in range(num_enemigos):
        # Movimiento del enemigo
        mar_x[i] += mar_x_cambio[i]

        # Cambiar dirección del enemigo si toca los bordes
        if mar_x[i] <= 0:
            mar_x_cambio[i] = 0.3
            mar_y[i] += mar_y_cambio[i]
        elif mar_x[i] >= 960:
            mar_x_cambio[i] = -0.3
            mar_y[i] += mar_y_cambio[i]

        # Verificar si ha habido una colisión
        if hay_colision(mar_x[i], mar_y[i], misil_x, misil_y):
            # Restablecer el misil
            misil_y = jugador_y
            misil_estado = False
            # Regenerar enemigo en una nueva posición
            mar_x[i] = random.randint(0, 960)
            mar_y[i] = random.randint(50, 150)

        # Dibujar el enemigo en pantalla
        enemigo(mar_x[i], mar_y[i], i)

    # Dibujar el jugador
    jugador_pos(jugador_x, jugador_y)

    # Actualizar la pantalla
    pygame.display.update()

    # Manejar eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            se_ejecuta = False

# Salir de pygame
pygame.quit()
