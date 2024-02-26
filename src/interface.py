import pygame
from engine import sprites
import config

class Interface:
    
    def draw_game_info(self, screen: pygame.surface.Surface, level_num, player_helthpoints, score):
        screen_width = config.get_value('screen_width')
        screen_height = config.get_value('screen_height')
        info_board_height = screen_width/6
        info_board_width = int(screen_height/3)
        font = pygame.font.Font('./fonts/BetterVCR.ttf',  int(info_board_height/6))
        font_score = pygame.font.Font('./fonts/BetterVCR.ttf',  int(info_board_height/3))
        font_level = pygame.font.Font('./fonts/BetterVCR.ttf',  int(info_board_height/3))
        
        level_text = font_level.render(f'Level {level_num+1}', 1, (255, 255, 0))
        level_text_pos = level_text.get_rect(center=(screen_width//2, 20))
        screen.blit(level_text, level_text_pos)
        
        hp_board = pygame.Surface((info_board_width, info_board_height))
        hp_board.fill((0, 0, 0))
        hp_text = font.render('Health', 1, (255, 255, 0))
        hp_text_pos = hp_text.get_rect(center=(info_board_width//2, info_board_height//5))
        hp_board.blit(hp_text, hp_text_pos)
        
        hearts_start_x = info_board_width-4*40-3*20
        hearts_start_y = info_board_height//1.6
        for i in range(0, player_helthpoints):
            health_point_rect = sprites.Sprites.health_point.get_rect(center=(hearts_start_x, hearts_start_y))
            hp_board.blit(sprites.Sprites.health_point, health_point_rect)
            hearts_start_x = hearts_start_x+40+20
        
        screen.blit(hp_board, (screen_width/2-int(screen_width/20)-info_board_width, 55))
        pygame.draw.rect(screen, (255, 255, 0), 
                         (screen_width/2-int(screen_width/20)-info_board_width, 55, info_board_width, info_board_height), 3)
        
        score_board = pygame.Surface((info_board_width, info_board_height))
        score_board.fill((0, 0, 0))
        score_text = font.render('Score', 1, (255, 255, 0))
        score_text_pos = score_text.get_rect(center=(info_board_width//2, info_board_height//5))
        score_board.blit(score_text, score_text_pos)
        
        score_count = font_score.render(f"{score:0>7}", 1, (255, 255, 0))
        score_count_pos = score_count.get_rect(center=(info_board_width//2, info_board_height//1.6))
        score_board.blit(score_count, score_count_pos)
        
        screen.blit(score_board, (screen_width/2+int(screen_width/20), 55))
        pygame.draw.rect(screen, (255, 255, 0), 
                         (screen_width/2+int(screen_width/20), 55, info_board_width, info_board_height), 3)
        
    def set_alpha_background(self, screen: pygame.surface.Surface):
        fon = pygame.Surface((650, 800))
        fon.fill((0, 0, 0))
        fon.set_alpha(100)
        screen.blit(fon, (0, 0))
        
    def call_pause_game_window(self, screen: pygame.surface.Surface):
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
        
    def call_complete_level_window(self, screen: pygame.surface.Surface, level_num):
        window_width = 300
        window_height = 150
        level_complete_window = pygame.Surface((window_width, window_height))
        level_complete_window.fill((0, 0, 0))
        level_complete_window_pos = level_complete_window.get_rect(center=(config.get_value('screen_width')//2, config.get_value('screen_height')//2))
        
        font = pygame.font.Font('./fonts/BetterVCR.ttf',  int(window_height/7))
        level_complete_text = font.render(f'Level {level_num+1} complete!', 1, (255, 255, 0))
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
        
    def call_complete_game_window(self, screen: pygame.surface.Surface, score):
        window_width = 300
        window_height = 150
        game_complete_window = pygame.Surface((window_width, window_height))
        game_complete_window.fill((0, 0, 0))
        game_complete_window_pos = game_complete_window.get_rect(center=(config.get_value('screen_width')//2, config.get_value('screen_height')//2))
        
        font = pygame.font.Font('./fonts/BetterVCR.ttf',  int(window_height/7))
        game_complete_text = font.render('Game complete!', 1, (255, 255, 0))
        game_complete_text_pos = game_complete_text.get_rect(center=(window_width//2, window_height/5))
        game_complete_window.blit(game_complete_text, game_complete_text_pos)
        
        game_complete_score = font.render(f'Total score: {score}', 1, (255, 255, 0))
        game_complete_score_pos = game_complete_score.get_rect(center=(window_width//2, window_height*2/5))
        game_complete_window.blit(game_complete_score, game_complete_score_pos)
        
        font_button = pygame.font.Font('./fonts/BetterVCR.ttf',  int(window_height/10))
        menu = font_button.render('1. Menu', 1, (255, 255, 0))
        menu_pos = menu.get_rect(center=(window_width//2, window_height*5/6))
        game_complete_window.blit(menu, menu_pos)
        
        screen.blit(game_complete_window, game_complete_window_pos)
        pygame.draw.rect(screen, (255, 255, 0),
                         (game_complete_window_pos.x, game_complete_window_pos.y, window_width, window_height), 3)