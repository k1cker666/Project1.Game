import pygame
import config

class Cell:
    cell_sprite_sheet = pygame.image.load('./images/sprites.png')
    
    def __init__(self):
        self.cell_width = config.get_value('cell_width')
        self.cell_height = config.get_value('cell_height')
    
    def draw():
        pass
    
class EmptyCell(Cell):
    def draw(self, screen, px, py):
        image = pygame.Surface((self.cell_width, self.cell_height))
        image.blit(self.cell_sprite_sheet, (0, 0), (0, 0, 40, 40))
        screen.blit(image, (px, py))

class FoodCell(Cell):
    def draw(self, screen, px, py):
        image = pygame.Surface((self.cell_width, self.cell_height))
        image.blit(self.cell_sprite_sheet, (0, 0), (40, 0, 80, 40))
        screen.blit(image, (px, py))
    
class BlockCell(Cell):
    def draw(self, screen, px, py):
        image = pygame.Surface((self.cell_width, self.cell_height))
        image.blit(self.cell_sprite_sheet, (0, 0), (80, 0, 120, 40))
        screen.blit(image, (px, py))