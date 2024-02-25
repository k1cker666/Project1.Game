from engine import text
from engine import sprites
import pygame

def print_menu(screen: pygame.surface.Surface):
    screen.blit(sprites.Sprites.background, (0, 0))
    text.draw_text("1. Start game.", 'Black', screen, 1/8, 1/10, 1/18)
    text.draw_text("2. Settings.", 'Black', screen, 1/8, 2/10, 1/18)
    text.draw_text("3. Quit.", 'Black', screen, 1/8, 3/10, 1/18)