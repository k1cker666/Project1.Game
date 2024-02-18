import menu
import pygame
from engine.board import board 
from enum import Enum, auto
import config
from engine.entity import player
from engine import sprites
from engine.board import cell

class StateManager(Enum):
    in_menu = auto()
    game_process = auto()
    
class GameManager:
    clock = pygame.time.Clock()
    game_state = StateManager.in_menu
    num = 0
    
    def __init__(self):
        self.FPS = config.get_value('FPS')
        level_name = self.change_level(self.num)
        self.board = board.Board(level_name)
        start_cell_px, start_cell_py = self.board.find_start_cell()
        self.player = player.Player(start_cell_px, start_cell_py)
        self.image = sprites.Image
                
    def run(self, screen):
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
                # self.player.interact()
                # self.player.get_score()
                # self.change_cell()
                self.draw_game_info(screen)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        return
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            self.game_state = StateManager.in_menu
                            self.player.player_direction = player.PlayerDirection.stay
                        if event.key == pygame.K_RIGHT:
                            self.player.player_direction = player.PlayerDirection.right
                        if event.key == pygame.K_LEFT:
                            self.player.player_direction = player.PlayerDirection.left
                        if event.key == pygame.K_DOWN:
                            self.player.player_direction = player.PlayerDirection.down
                        if event.key == pygame.K_UP:
                            self.player.player_direction = player.PlayerDirection.up
            pygame.display.update()
            self.clock.tick(self.FPS)

    def change_level(self, num):
        level_list = config.get_value('levels')
        level_name = level_list[num]['map_file']
        self.num +=1
        return level_name
        
    def draw_game_info(self, screen):
        screen_width = config.get_value('screen_width')
        screen_height = config.get_value('screen_height')
        info_board_height = screen_width/5
        info_board_width = int(screen_height/3)
        font = pygame.font.Font('./fonts/BetterVCR.ttf',  int(info_board_height/6))
        font_score = pygame.font.Font('./fonts/BetterVCR.ttf',  int(info_board_height/3))
        
        hp_board = pygame.Surface((info_board_width, info_board_height))
        hp_board.fill((0, 0, 0))
        hp_text = font.render('Healh', 1, (255, 255, 0))
        hp_text_pos = hp_text.get_rect(center=(info_board_width//2, info_board_height//5))
        hp_board.blit(hp_text, hp_text_pos)
        
        hearts_start_x = info_board_width-4*40-3*20
        hearts_start_y = info_board_height//1.6
        for i in range(0, self.player.helthpoints):
            health_point_rect = self.image.health_point.get_rect(center=(hearts_start_x, hearts_start_y))
            hp_board.blit(self.image.health_point, health_point_rect)
            hearts_start_x = hearts_start_x+40+20
        
        screen.blit(hp_board, (screen_width/2-int(screen_width/20)-info_board_width, 20))
        pygame.draw.rect(screen, (255, 255, 0), 
                         (screen_width/2-int(screen_width/20)-info_board_width, 20, info_board_width, info_board_height), 3)
        
        score_board = pygame.Surface((info_board_width, info_board_height))
        score_board.fill((0, 0, 0))
        score_text = font.render('Score', 1, (255, 255, 0))
        score_text_pos = score_text.get_rect(center=(info_board_width//2, info_board_height//5))
        score_board.blit(score_text, score_text_pos)
        
        score_count = font_score.render(f"{self.player.score:0>7}", 1, (255, 255, 0))
        score_count_pos = score_count.get_rect(center=(info_board_width//2, info_board_height//1.6))
        score_board.blit(score_count, score_count_pos)
        
        screen.blit(score_board, (screen_width/2+int(screen_width/20), 20))
        pygame.draw.rect(screen, (255, 255, 0), 
                         (screen_width/2+int(screen_width/20), 20, info_board_width, info_board_height), 3)
        
    # def change_cell(self):
    #     if self.player.event == player.PlayerEvent.FoodEvent:
    #         self.board.game_map[self.player.coords[1]][self.player.coords[0]] = cell.EmptyCell()