import pygame
import config
from engine import image

class Cell:
    image = image.Image
    
    def __init__(self):
        self.cell_width = config.get_value('cell_width')
        self.cell_height = config.get_value('cell_height')
    
    def draw():
        pass
    
class EmptyCell(Cell):
    def draw(self, screen, px, py):
        # image = pygame.Surface((self.cell_width, self.cell_height))
        # image.blit(self.image.empty_cell, (0, 0), (0, 0, 40, 40))
        screen.blit(self.image.empty_cell, (px, py))

class FoodCell(Cell):
    def draw(self, screen, px, py):
        # image = pygame.Surface((self.cell_width, self.cell_height))
        # image.blit(self.image.food_cell, (0, 0), (40, 0, 80, 40))
        screen.blit(self.image.food_cell, (px, py))
    
class BlockCell(Cell):
    def draw(self, screen, px, py):
        # image = pygame.Surface((self.cell_width, self.cell_height))
        # image.blit(self.image.block_cell, (0, 0), (80, 0, 120, 40))
        screen.blit(self.image.block_cell, (px, py))
        
class StartCell(Cell):
    def draw(self, screen, px, py):
        # image = pygame.Surface((self.cell_width, self.cell_height))
        # image.blit(self.image.empty_cell, (0, 0), (0, 0, 40, 40))
        screen.blit(self.image.empty_cell, (px, py))
