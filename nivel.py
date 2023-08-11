import pygame
import sys

pygame.init()

font = pygame.font.SysFont("Arial", 20)
# Colores
moccasin = (255, 228, 181)
BLACK = (0, 0, 0)

def seleccionar_nivel():
    level_screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Selección de Nivel")

    level_texts = [
        font.render("Fácil", True, BLACK),
        font.render("Difícil", True, BLACK),
        font.render("Volver", True, BLACK)
    ]

    level_rects = [
        level_texts[0].get_rect(center=(400, 250)),
        level_texts[1].get_rect(center=(400, 300)),
        level_texts[2].get_rect(center=(400, 350))
    ]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for i, rect in enumerate(level_rects):
                    if rect.collidepoint(pygame.mouse.get_pos()):
                        if i == 0:
                            return 20
                        elif i == 1:
                            return 30
                        elif i == 2:
                            return None

        level_screen.fill(moccasin)
        for text, rect in zip(level_texts, level_rects):
            level_screen.blit(text, rect)
        pygame.display.flip()
