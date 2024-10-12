'''programar juego invasion espacial'''

from turtle import *
import pygame


#inicializar pygame
pygame.init()
se_ejecuta = True

# Configuracion de la ventana
pantalla = pygame.display.set_mode((1024, 768))


pygame.display.set_caption('Invasion Espacial')
icono = pygame.image.load('ovni.png')
pygame.display.set_icon(icono)



#loop juego
while se_ejecuta:
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            se_ejecuta = False

    
        