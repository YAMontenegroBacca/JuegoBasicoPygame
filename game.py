import pygame
import sys
import random

pygame.init()

#Configuración Ventana
ancho_ventana = 800
alto_ventana = 700
ventana = pygame.display.set_mode((ancho_ventana, alto_ventana))
color_ventana = (34, 139, 34)
darkred = (139, 0, 0)
ghostwhite = (248, 248, 255)
black = (0, 0, 0)


#Configuración Jugador
colorJugador = (255, 250, 240)
tam_jugador = 50
pos_jugador = [ancho_ventana/2,alto_ventana/2]


#Configuración Enemigo 1
color_En1 = (139, 0, 0)
tam_ene1 = 60
pos_En1 = [random.randint(0, ancho_ventana- tam_ene1),0]


#Configuración Enemigo 2
color_En2 = (139, 0, 0)
tam_ene2 = 60
pos_En2 = [random.randint(0, ancho_ventana- tam_ene2),alto_ventana-tam_ene2]

font = pygame.font.SysFont("Arial", 40)
# fin del juego
game_over_message = font.render("¡Fin del Juego!", True, black)
game_over_rect = game_over_message.get_rect(center=(400, 300))

#------------- Funciones -----------------

def choque_borde(pos_j,tam_j):
    x = pos_j[0]
    y = pos_j[1]
    if y <= 0+tam_j:
        return True
    elif y >= alto_ventana-tam_j:
        return True
    elif x <= 0+tam_jugador:
        return True
    elif x >= ancho_ventana-tam_j:
        return True
    return False

def mover_jugador(evento):
    if evento.type == pygame.KEYDOWN:
        x = pos_jugador[0]
        y = pos_jugador[1]
                
        if y >= 0+tam_jugador and y < alto_ventana-tam_jugador:
            if evento.key == pygame.K_UP:
                y -= tam_jugador
            if evento.key == pygame.K_DOWN:
                y += tam_jugador
        
        if x >=0 and y < ancho_ventana:
            if evento.key == pygame.K_LEFT:
                x -= tam_jugador
            if evento.key == pygame.K_RIGHT:
                x += tam_jugador
        
        pos_jugador[1]=y
        pos_jugador[0]=x

    ventana.fill(color_ventana)
    

def mover_enemigo(pos_en, tam_en):
    if pos_en[1] >= 0 and pos_en[1] < alto_ventana:
        pos_en[1] += tam_en
        
    else:
        pos_en[0] = random.randint(0, ancho_ventana - tam_en)
        pos_en[1] = 0
    return pos_en
        


def choque(pos_j, pos_e, tam_j, tam_e):
    #obtener posiciones
    p_Jx = pos_j[0]
    p_Jy = pos_j[1]
    p_Ex = pos_e[0]
    p_Ey = pos_e[1]

    en_jug_X = (p_Ex >= p_Jx and p_Ex < (p_Jx + tam_j))
    jug_en_X = (p_Jx >= p_Ex and p_Jx < (p_Ex + tam_e))
    en_jug_Y = (p_Ey >= p_Jy and p_Ey < (p_Jy + tam_j))
    jug_en_Y = (p_Jy >= p_Ey and p_Jy < (p_Ey + tam_e))

    #Validaciones
    if (en_jug_X or jug_en_X):
        if (en_jug_Y or jug_en_Y):
            return True
    return False


def show_game_over():
    ventana.fill(darkred)
    ventana.blit(game_over_message, game_over_rect)
    pygame.display.flip()

# ------------ Ciclo Principal Del Juego----------------

def iniciar_juego (speed):
    jugando = True
    velocidad = pygame.time.Clock() 
    while jugando:
        for event in pygame.event.get():
            
            #Finalizar juego al cerrarlo
            if (event.type == pygame.QUIT):
                jugando = False

            #Mover el jugador   
            mover_jugador(event)
            
            #MOVER ENEMIGO1
            mover_enemigo(pos_En1, tam_ene1)
            #MOVER ENEMIGO2
            mover_enemigo(pos_En2, tam_ene2)

            #Fin del juego
            if choque_borde(pos_jugador, tam_jugador):
                show_game_over()
                pygame.time.wait(2000)
                jugando = False
            if choque(pos_jugador, pos_En1, tam_jugador, tam_ene1):
                show_game_over()
                pygame.time.wait(2000)
                jugando = False
            if choque(pos_jugador, pos_En2, tam_jugador, tam_ene2):
                show_game_over()
                pygame.time.wait(2000)
                jugando = False
            



        #DibujarJugador
        pygame.draw.rect(ventana, colorJugador, (pos_jugador[0], pos_jugador[1], tam_jugador,tam_jugador))
        
        #DibujarEnemigo1
        pygame.draw.rect(ventana, color_En1, (pos_En1[0], pos_En1[1], tam_ene1,tam_ene1))
        
        #DibujarEnemigo2
        pygame.draw.rect(ventana, color_En2, (pos_En2[0], pos_En2[1], tam_ene2,tam_ene2))
        velocidad.tick(speed)
        pygame.display.update()


    # Cerrar Pygame
    pygame.quit()
    sys.exit()

            