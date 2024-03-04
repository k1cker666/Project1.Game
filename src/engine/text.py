import pygame
import config
import os
from resouce_path import resource_path

def draw_text(text, color, screen, width_coef, height_coef, size_font_coef):
    height = config.get_value('screen_height')
    width = config.get_value('screen_width')
    font = pygame.font.Font(resource_path(os.path.join('fonts', 'BetterVCR.ttf')),  int(height * size_font_coef))
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (int(width*width_coef), int(height*height_coef)))