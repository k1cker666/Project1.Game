import json
from engine.board  import cell
import pygame
import config


class Board:
    game_map: list
    
    def load(self, level_name):
        file_path = str("././config/maps/"+level_name)
        file_map = open(file_path, 'r')
        game_map = json.loads(file_map.read()) # game_map хочется чтобы не изменялся
        file_map.close()
        self.game_map = game_map.copy()
        px = 0
        py = 0
        for line in self.game_map:
            for item in line:
                if item == 0:
                    self.game_map[py][px] = cell.BlockCell()
                    px += 1
                elif item == 1:
                    self.game_map[py][px] = cell.EmptyCell()
                    px += 1
                elif item == 2:
                    self.game_map[py][px] = cell.FoodCell()
                    px += 1
                if px == len(game_map[0]):
                    px = 0
                    py += 1
                    
    def draw(self, screen):
        screen_width = config.get_value('screen_width')
        screen_height = config.get_value('screen_height')
        cell_width = cell_height = screen_height / 20
        start_x = screen_width/2 - cell_width*len(self.game_map[0])/2
        start_y = screen_height/2 - cell_height*len(self.game_map)/2
        for y, line in enumerate(self.game_map):
            py = y*cell_width+start_y
            for x, item in enumerate(line):
                px = x*cell_width+start_x
                item.draw(screen, px, py)
        pygame.display.flip()