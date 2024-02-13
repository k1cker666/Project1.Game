from engine.board import board 
import config
from engine.board.cell import Cell
import pygame

class Player:
    move_right = [(0, 40, 40, 80), (40, 40, 80, 80), (80, 40, 120, 80)]
    move_left = [(0, 80, 40, 120), (40, 80, 80, 120), (80, 80, 120, 120)]
    move_down = [(0, 120, 40, 160), (40, 120, 80, 160), (80, 120, 120, 160)]
    move_up = [(0, 160, 40, 200), (40, 160, 80, 200), (80, 120, 120, 200)]
    
    def __init__(self, start_cell_px, start_cell_py):
        self.start_cell_px = start_cell_px
        self.start_cell_py = start_cell_py
        # self.start_board_x = self.screen_width/2 - self.cell_width*len(board.Board.game_map[0])/2
        # self.start_board_y = self.screen_height/2 - self.cell_height*len(board.Board.game_map)/2
        
    def find_player_start_coordinates(self):
        screen_width = config.get_value('screen_width')
        screen_height = config.get_value('screen_height')
        self.cell_width = self.cell_height = screen_height/20
        start_board_x = screen_width/2 - self.cell_width*15/2
        start_board_y = screen_height/2 - self.cell_height*15/2
        self.start_cell_x = start_board_x + self.start_cell_px*self.cell_width
        self.start_cell_y = start_board_y + self.start_cell_py*self.cell_height
    
    def draw(self, screen):
        self.find_player_start_coordinates()
        image = pygame.Surface((self.cell_width, self.cell_height))
        image.blit(Cell.sprite_sheet, (0, 0), (120, 0, 160, 40))
        screen.blit(image, (self.start_cell_x, self.start_cell_y))
        
    def moving_right(self, screen):
        i = 0
        while True:
            image = pygame.Surface((self.cell_width, self.cell_height))
            image.blit(Cell.sprite_sheet, (0, 0), self.move_right[i])
            screen.blit(image, (self.start_cell_x, self.start_cell_y))
            i += 1
            if i == 2:
                i = 0