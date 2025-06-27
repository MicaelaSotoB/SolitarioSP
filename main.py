import pygame, sys
from constantes import *

pygame.init()

pantalla = pygame.display.set_mode((800, 500))
pygame.display.set_caption("Solitario")
clock=pygame.time.Clock()

color=(100,30,100)

cursor_nuevo = pygame.image.load('modulos/materiales/cursor_pointer.png')
cursor_nuevo = pygame.transform.scale(cursor_nuevo, (50, 50))
pygame.mouse.set_visible(False)
icon=pygame.image.load("modulos/materiales/iconosolitario.png") #Carga la imagen 
pygame.display.set_icon(icon) #Coloca el icono
fondomenu = pygame.image.load('modulos/materiales/fondomenu.png')
fondomenu= pygame.transform.scale(fondomenu,(800,500))
titulo=pygame.image.load("modulos/materiales/solitarioTitulo.png")
titulo=pygame.transform.scale(titulo, (410, 250))
fuente = pygame.font.Font("modulos/materiales/pixel.ttf", 48)
volumen=pygame.image.load("modulos/materiales/MusicNotes.png")
volumen=pygame.transform.scale(volumen, (50, 50))

seguir = True
while seguir:
    pantalla.blit(fondomenu, [0, 0])

    opcion_jugar=pygame.draw.rect(pantalla, COLOR_OPCIONES,
                    pygame.Rect(235, 240, 310, 70), border_radius=RADIO_BORDES)
    opcion_salir=pygame.draw.rect(pantalla, COLOR_OPCIONES,
                    pygame.Rect(244, 330, 293, 50), border_radius=RADIO_BORDES)
    pantalla.blit(titulo, (183, 30))

    texto_jugar=fuente.render("Jugar", True,  (0, 0, 0), None)
    texto_rect = texto_jugar.get_rect(center=opcion_jugar.center)
    pantalla.blit(volumen, (30, 430))

    pantalla.blit(texto_jugar, texto_rect)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    clock.tick(60)

    pos = pygame.mouse.get_pos()
    pantalla.blit(cursor_nuevo, pos)
    
    pygame.display.update()