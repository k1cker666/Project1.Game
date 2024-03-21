import menu
import pygame
from engine.board import board 
from enum import Enum, auto
import config
from engine.entity import player
from engine.entity import direction
from interface import Interface
from engine.entity import enemy
from engine.entity import area

class StateManager(Enum):
    in_menu = auto()
    game_process = auto()
    level_complete_window = auto()
    pause = auto()
    game_comlete = auto()
    game_over = auto()
    game_quit = auto()
    
class GameManager:
    clock = pygame.time.Clock()
    game_state = StateManager.in_menu
    level_num = 0
    interface = Interface()
    
    def __init__(self, sounds: dict):
        self.FPS = config.get_value('FPS')
        level_name = self.get_level(self.level_num)
        self.board = board.Board(level_name)
        self.player = player.Player()
        self.player.set_spawn_coord(self.board.get_player_start_cell())
        self.enemy_innit()
        self.sounds = sounds
    
    def run(self, screen: pygame.surface.Surface):
        while True:
            if self.game_state == StateManager.in_menu:
                self.print_menu(screen)
            if self.game_state == StateManager.game_process:
                self.game_initialization(screen)
            if self.game_state == StateManager.level_complete_window:
                self.call_level_complite_window(screen)    
            if self.game_state == StateManager.pause:
                self.call_pause_game_window(screen)
            if self.game_state == StateManager.game_comlete:
                self.call_complete_game_window(screen)
            if self.game_state == StateManager.game_over:
                self.call_game_over_window(screen)
            if self.game_state == StateManager.game_quit:
                return
            pygame.display.flip()
            self.clock.tick(self.FPS)
                    
    def enemy_innit(self):
        blinky = enemy.Enemy(area.Area.areaA)
        clyde = enemy.Enemy(area.Area.areaB)
        inky = enemy.Enemy(area.Area.areaC)
        pinky = enemy.Enemy(area.Area.areaD)
        self.enemies = [blinky, clyde, inky, pinky]
        start_cells = self.board.get_enemy_start_cell()
        for unit in self.enemies:
            unit.set_spawn_coord(start_cells)
            
    def handle_player_event(self):
        if self.player.event.type_event == player.PlayerEventType.NoEvent:
            return
        elif self.player.event.type_event == player.PlayerEventType.FoodEvent:
            self.board.set_empty_cell(self.player.event.context['coords'])
            self.player.clear_event()
            self.sounds['food'].play()
        elif self.player.event.type_event == player.PlayerEventType.EnemyAttack:
            self.player.clear_event()
            self.sounds['enemy_attack'].play()

    def print_menu(self, screen: pygame.surface.Surface):
        menu.print_menu(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_state = StateManager.game_quit
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    self.game_state = StateManager.game_process
                if event.key == pygame.K_3:
                    self.game_state = StateManager.game_quit
    
    def game_initialization(self, screen: pygame.surface.Surface):
        screen.fill((0, 0, 0))
        self.board.draw(screen)
        
        for unit in self.enemies:
            unit.draw(screen)
            unit.move(self.board.is_block_ahead(), self.board.get_free_direction(), self.board.is_own_area())
            self.player.interact_enemy(unit.get_rect_xy())
        self.player.draw(screen)
        self.player.move(self.board.is_block_ahead())
        self.player.interact_cell(self.board.get_cell(self.player.get_coord()))
        self.handle_player_event()
        self.interface.draw_game_info(screen, self.level_num, self.player.helthpoints, self.player.total_score)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_state = StateManager.game_quit
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.interface.set_alpha_background(screen)
                    self.game_state = StateManager.pause
                if event.key == pygame.K_RIGHT:
                    self.player.change_direction(direction.Direction.right)
                if event.key == pygame.K_LEFT:
                    self.player.change_direction(direction.Direction.left)
                if event.key == pygame.K_DOWN:
                    self.player.change_direction(direction.Direction.down)
                if event.key == pygame.K_UP:
                    self.player.change_direction(direction.Direction.up)
                if event.key == pygame.K_0:
                    self.board.admin_clear_food_cells()
        if self.board.check_food_cells():
            self.interface.set_alpha_background(screen)
            self.sounds['level_up'].play()
            if self.check_levels():
                self.game_state = StateManager.game_comlete
            else:
                self.game_state = StateManager.level_complete_window
        if self.player.helthpoints == 0:
            self.interface.set_alpha_background(screen)
            self.game_state = StateManager.game_over
            
    def call_level_complite_window(self, screen: pygame.surface.Surface):
        self.player.change_direction(direction.Direction.stay)
        self.interface.call_complete_level_window(screen, self.level_num)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    self.turn_next_level()
                if event.key == pygame.K_2:
                    self.restart_level()
                if event.key == pygame.K_3:
                    self.game_state = StateManager.in_menu
            if event.type == pygame.QUIT:
                self.game_state = StateManager.game_quit
    
    def call_pause_game_window(self, screen: pygame.surface.Surface):
        self.player.change_direction(direction.Direction.stay)
        self.interface.call_pause_game_window(screen)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1 or event.key == pygame.K_ESCAPE:
                    self.game_state = StateManager.game_process
                if event.key == pygame.K_2:
                    self.game_state = StateManager.in_menu
            if event.type == pygame.QUIT:
                self.game_state = StateManager.game_quit
    
    def call_complete_game_window(self, screen: pygame.surface.Surface):
        self.interface.call_complete_game_window(screen, self.player.total_score)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_state = StateManager.game_quit
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    self.game_state = StateManager.in_menu
        
    def call_game_over_window(self, screen: pygame.surface.Surface):
        self.interface.call_game_over_window(screen, self.player.total_score)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_state = StateManager.game_quit
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    self.restart_game()
                    self.game_state = StateManager.in_menu
     
    def respawn_enemies(self):
        start_cells = self.board.get_enemy_start_cell()
        for unit in self.enemies:
            unit.clear_delay_timer()
            unit.set_spawn_coord(start_cells)
            unit.enemy_direction = direction.Direction.no_direction
            
    def get_level(self, level_num):
        level_list = config.get_value('levels')
        level_name = level_list[level_num]['map_file']
        return level_name

    def turn_next_level(self):
        self.level_num +=1
        level_name = self.get_level(self.level_num)
        self.board = board.Board(level_name)
        self.player.set_spawn_coord(self.board.get_player_start_cell())
        self.player.clear_curr_level_score()
        self.respawn_enemies()
        self.game_state = StateManager.game_process
        
    def restart_level(self):
        self.player.total_score -= self.player.curr_level_score
        self.player.clear_curr_level_score()
        self.respawn_enemies()
        level_name = self.get_level(self.level_num)
        self.board = board.Board(level_name)
        self.player.set_spawn_coord(self.board.get_player_start_cell())
        self.game_state = StateManager.game_process
        
    def restart_game(self):
        self.level_num = 0
        self.player.clear_start_stats()
        self.respawn_enemies()
        level_name = self.get_level(self.level_num)
        self.board = board.Board(level_name)
        self.player.set_spawn_coord(self.board.get_player_start_cell())
        self.player.player_direction = direction.Direction.stay
    
    def check_levels(self):
        count_of_levels = len(config.get_value('levels'))
        return (count_of_levels == (self.level_num+1))