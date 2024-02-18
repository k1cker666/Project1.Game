import json
from engine.board import cell
import pygame
import config

class Board:
    game_map: list
    
    def __init__(self, level_name):
        file_path = str("././config/maps/"+level_name)
        file_map = open(file_path, 'r')
        game_map_json = json.loads(file_map.read())
        file_map.close()
        self.game_map = game_map_json.copy()
        self.screen_width = config.get_value('screen_width')
        self.screen_height = config.get_value('screen_height')
        self.cell_width = self.cell_height = self.screen_height / 20
        self.start_x = self.screen_width/2 - self.cell_width*len(self.game_map[0])/2
        self.start_y = self.screen_height/2 - self.cell_height*len(self.game_map)/2 + 3*self.screen_height/32
        self.load()
        
    def load(self):
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
                elif item == 3:
                    self.game_map[py][px] = cell.StartCell()
                    px += 1
                if px == len(self.game_map[0]):
                    px = 0
                    py += 1
                    
    def draw(self, screen):
        for y, line in enumerate(self.game_map):
            py = y*self.cell_width+self.start_y
            for x, item in enumerate(line):
                px = x*self.cell_width+self.start_x
                item.draw(screen, px, py)
        
    def find_start_cell(self):
        for py in range(len(self.game_map)):
            for px in range(len(self.game_map[py])):
                if isinstance(self.game_map[py][px], cell.StartCell):
                    return (px, py)
    
    # def get_cell(self, coord):
    #     return self.game_map[coord[1]][coord[0]]