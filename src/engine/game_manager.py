import menu
import pygame
from engine.board import board 
from enum import Enum, auto
import config
from engine.entity import player
from engine import sprites
from engine.board import cell
import time

class StateManager(Enum):
    in_menu = auto()
    game_process = auto()
    level_complete_window = auto()
    pause = auto()
    
class GameManager:
    clock = pygame.time.Clock()
    game_state = StateManager.in_menu
    num = 0
    
    def __init__(self):
        self.FPS = config.get_value('FPS')
        level_name = self.change_level(self.num)
        self.board = board.Board(level_name)
        self.player = player.Player()
        start_cell_px, start_cell_py = self.board.find_start_cell()
        self.player.set_spawn_coord(start_cell_px, start_cell_py)
        self.image = sprites.Image
                
    def run(self, screen: pygame.surface.Surface):
        while True:
            if self.game_state == StateManager.in_menu:
                screen.blit(self.image.background, (0, 0))
                menu.print_menu(screen)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                         return
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_1:
                            self.game_state = StateManager.game_process
                        if event.key == pygame.K_3:
                            return 
            if self.game_state == StateManager.game_process:
                screen.fill((0, 0, 0))
                self.board.draw(screen)
                self.player.draw(screen)
                self.player.move()
                self.player.interact(self.board.get_cell(self.player.get_coord()))
                self.handle_player_event()
                self.draw_game_info(screen)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        return
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            self.set_alpha_background(screen)
                            self.game_state = StateManager.pause
                        if event.key == pygame.K_RIGHT:
                            self.player.change_direction(1)
                        if event.key == pygame.K_LEFT:
                            self.player.change_direction(2)
                        if event.key == pygame.K_DOWN:
                            self.player.change_direction(3)
                        if event.key == pygame.K_UP:
                            self.player.change_direction(4)
                        if event.key == pygame.K_0:
                            self.board.admin_clear_food_cells()
                if self.board.check_food_cells():
                    self.set_alpha_background(screen)
                    self.game_state = StateManager.level_complete_window
            if self.game_state == StateManager.level_complete_window:
                self.call_complete_level_window(screen)
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_1:
                            self.turn_next_level()
                        if event.key == pygame.K_2:
                            self.restart_level()
                        if event.key == pygame.K_3:
                            self.game_state = StateManager.in_menu
                    if event.type == pygame.QUIT:
                        return
            if self.game_state == StateManager.pause:
                self.call_pause_game_window(screen)
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_1 or event.key == pygame.K_ESCAPE:
                            self.game_state = StateManager.game_process
                        if event.key == pygame.K_2:
                            self.game_state = StateManager.in_menu
                    if event.type == pygame.QUIT:
                        return
            pygame.display.flip()
            self.clock.tick(self.FPS)

    def change_level(self, num):
        level_list = config.get_value('levels')
        level_name = level_list[num]['map_file']
        self.num +=1
        return level_name
        
    def draw_game_info(self, screen: pygame.surface.Surface):
        screen_width = config.get_value('screen_width')
        screen_height = config.get_value('screen_height')
        info_board_height = screen_width/6
        info_board_width = int(screen_height/3)
        font = pygame.font.Font('./fonts/BetterVCR.ttf',  int(info_board_height/6))
        font_score = pygame.font.Font('./fonts/BetterVCR.ttf',  int(info_board_height/3))
        font_level = pygame.font.Font('./fonts/BetterVCR.ttf',  int(info_board_height/3))
        
        level_text = font_level.render(f'Level {self.num}', 1, (255, 255, 0))
        level_text_pos = level_text.get_rect(center=(screen_width//2, 20))
        screen.blit(level_text, level_text_pos)
        
        hp_board = pygame.Surface((info_board_width, info_board_height))
        hp_board.fill((0, 0, 0))
        hp_text = font.render('Health', 1, (255, 255, 0))
        hp_text_pos = hp_text.get_rect(center=(info_board_width//2, info_board_height//5))
        hp_board.blit(hp_text, hp_text_pos)
        
        hearts_start_x = info_board_width-4*40-3*20
        hearts_start_y = info_board_height//1.6
        for i in range(0, self.player.helthpoints):
            health_point_rect = self.image.health_point.get_rect(center=(hearts_start_x, hearts_start_y))
            hp_board.blit(self.image.health_point, health_point_rect)
            hearts_start_x = hearts_start_x+40+20
        
        screen.blit(hp_board, (screen_width/2-int(screen_width/20)-info_board_width, 55))
        pygame.draw.rect(screen, (255, 255, 0), 
                         (screen_width/2-int(screen_width/20)-info_board_width, 55, info_board_width, info_board_height), 3)
        
        score_board = pygame.Surface((info_board_width, info_board_height))
        score_board.fill((0, 0, 0))
        score_text = font.render('Score', 1, (255, 255, 0))
        score_text_pos = score_text.get_rect(center=(info_board_width//2, info_board_height//5))
        score_board.blit(score_text, score_text_pos)
        
        score_count = font_score.render(f"{self.player.score:0>7}", 1, (255, 255, 0))
        score_count_pos = score_count.get_rect(center=(info_board_width//2, info_board_height//1.6))
        score_board.blit(score_count, score_count_pos)
        
        screen.blit(score_board, (screen_width/2+int(screen_width/20), 55))
        pygame.draw.rect(screen, (255, 255, 0), 
                         (screen_width/2+int(screen_width/20), 55, info_board_width, info_board_height), 3)
                    
    def handle_player_event(self):
        if self.player.event.type_event == player.PlayerEventType.FoodEvent:
            self.board.set_empty_cell(self.player.event.context['coords'])
            self.player.clear_event()
    
    def call_complete_level_window(self, screen: pygame.surface.Surface):
        self.player.change_direction(0)
        
        window_width = 300
        window_height = 150
        level_complete_window = pygame.Surface((window_width, window_height))
        level_complete_window.fill((0, 0, 0))
        level_complete_window_pos = level_complete_window.get_rect(center=(config.get_value('screen_width')//2, config.get_value('screen_height')//2))
        
        font = pygame.font.Font('./fonts/BetterVCR.ttf',  int(window_height/7))
        level_complete_text = font.render(f'Level {self.num} complete!', 1, (255, 255, 0))
        level_complete_text_pos = level_complete_text.get_rect(center=(window_width//2, window_height/5))
        level_complete_window.blit(level_complete_text, level_complete_text_pos)
        
        font_button = pygame.font.Font('./fonts/BetterVCR.ttf',  int(window_height/10))
        next_level = font_button.render('1. Next level', 1, (255, 255, 0))
        next_level_pos = next_level.get_rect(center=(window_width//2, window_height*4/8))
        level_complete_window.blit(next_level, next_level_pos)
        
        restart_level = font_button.render('2. Restart level', 1, (255, 255, 0))
        restart_level_pos = restart_level.get_rect(center=(window_width//2, window_height*5/8))
        level_complete_window.blit(restart_level, restart_level_pos)
        
        menu = font_button.render('3. Menu', 1, (255, 255, 0))
        menu_pos = menu.get_rect(center=(window_width//2, window_height*6/8))
        level_complete_window.blit(menu, menu_pos)
        
        screen.blit(level_complete_window, level_complete_window_pos)
        pygame.draw.rect(screen, (255, 255, 0),
                         (level_complete_window_pos.x, level_complete_window_pos.y, window_width, window_height), 3)
    
    def call_pause_game_window(self, screen: pygame.surface.Surface):
        self.player.change_direction(0)
        
        window_width = 300
        window_height = 150
        level_complete_window = pygame.Surface((window_width, window_height))
        level_complete_window.fill((0, 0, 0))
        level_complete_window_pos = level_complete_window.get_rect(center=(config.get_value('screen_width')//2, config.get_value('screen_height')//2))
        
        font = pygame.font.Font('./fonts/BetterVCR.ttf',  int(window_height/7))
        level_complete_text = font.render('Game paused', 1, (255, 255, 0))
        level_complete_text_pos = level_complete_text.get_rect(center=(window_width//2, window_height/5))
        level_complete_window.blit(level_complete_text, level_complete_text_pos)
        
        font_button = pygame.font.Font('./fonts/BetterVCR.ttf',  int(window_height/10))
        resume = font_button.render('1. Resume', 1, (255, 255, 0))
        resume_pos = resume.get_rect(center=(window_width//2, window_height*3/6))
        level_complete_window.blit(resume, resume_pos)
        
        menu = font_button.render('2. Menu', 1, (255, 255, 0))
        menu_pos = menu.get_rect(center=(window_width//2, window_height*4/6))
        level_complete_window.blit(menu, menu_pos)
        
        screen.blit(level_complete_window, level_complete_window_pos)
        pygame.draw.rect(screen, (255, 255, 0),
                         (level_complete_window_pos.x, level_complete_window_pos.y, window_width, window_height), 3)
        
    def set_alpha_background(self, screen: pygame.surface.Surface):
        fon = pygame.Surface((650, 800))
        fon.fill((0, 0, 0))
        fon.set_alpha(100)
        screen.blit(fon, (0, 0))
        
    def turn_next_level(self):
        level_name = self.change_level(self.num)
        self.board = board.Board(level_name)
        start_cell_px, start_cell_py = self.board.find_start_cell()
        self.player.set_spawn_coord(start_cell_px, start_cell_py)
        self.player.clear_score_count()
        self.game_state = StateManager.game_process
        
    def restart_level(self):
        self.num -= 1
        self.player.score -= 50*self.player.score_count
        self.player.clear_score_count()
        level_name = self.change_level(self.num)
        self.board = board.Board(level_name)
        start_cell_px, start_cell_py = self.board.find_start_cell()
        self.player.set_spawn_coord(start_cell_px, start_cell_py)
        self.game_state = StateManager.game_process