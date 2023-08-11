import pygame
import sys
from game import iniciar_juego 
from nivel import seleccionar_nivel

pygame.init()

#Configuración Ventana
ancho_ventana = 800
alto_ventana = 700
ventana = pygame.display.set_mode((ancho_ventana, alto_ventana))
pygame.display.set_caption("Esquivando al Enemigo")
color_ventana = (245, 255, 250)
ventana.fill(color_ventana)

# fuente
font = pygame.font.SysFont("Arial", 20)

# opciones menú
opc_jugar = font.render("Iniciar", True, (0, 0, 0))
opc_selec_nivel = font.render("Seleccionar Nivel", True, (0, 0, 0))
opc_salir = font.render("Salir", True, (0, 0, 0))

rect_jugar = opc_jugar.get_rect(center=(400, 250))
react_nivel = opc_selec_nivel.get_rect(center=(400, 300))
rect_salir = opc_salir.get_rect(center=(400, 350))


nivel = 10
while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if rect_jugar.collidepoint(pygame.mouse.get_pos()):
                print(nivel)
                iniciar_juego(nivel)
            elif react_nivel.collidepoint(pygame.mouse.get_pos()):
                nivel = seleccionar_nivel()
                print(nivel)
            elif rect_salir.collidepoint(pygame.mouse.get_pos()):
                pygame.quit()
                sys.exit()

    ventana.fill(color_ventana)
    
    # Dibujar textos en la pantalla
    ventana.blit(opc_jugar, rect_jugar)
    ventana.blit(opc_selec_nivel, react_nivel)
    ventana.blit(opc_salir, rect_salir)
    
    pygame.display.flip()