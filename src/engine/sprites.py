import pygame
import os
from resouce_path import resource_path

def load_image(image_name):
    result = pygame.image.load(image_name)
    result.set_colorkey((255, 255, 255))
    return result 

def load_image_black_bg(image_name):
    result = pygame.image.load(image_name)
    result.set_colorkey((0, 0, 0))
    return result 

class Sprites:
    background = pygame.image.load(resource_path(os.path.join('images', 'testbg.png')))
    block_cell = pygame.image.load(resource_path(os.path.join('images', 'sprites', 'BlockCell.png')))
    empty_cell = pygame.image.load(resource_path(os.path.join('images', 'sprites', 'EmptyCell.png')))
    food_cell = pygame.image.load(resource_path(os.path.join('images', 'sprites', 'FoodCell.png')))
    
    health_point = load_image(resource_path(os.path.join('images', 'sprites', 'HP.png')))
    health_point = pygame.transform.scale(health_point, (50, 50))
    
    player_stay = load_image(resource_path(os.path.join('images', 'sprites', 'player', 'Stay.png')))
    
    player_right_1 = load_image(resource_path(os.path.join('images', 'sprites', 'player', 'Right_1.png')))
    player_right_2 = load_image(resource_path(os.path.join('images', 'sprites', 'player', 'Right_2.png')))
    player_right_3 = load_image(resource_path(os.path.join('images', 'sprites', 'player', 'Right_3.png')))
    
    player_left_1 = load_image(resource_path(os.path.join('images', 'sprites', 'player', 'Left_1.png')))
    player_left_2 = load_image(resource_path(os.path.join('images', 'sprites', 'player', 'Left_2.png')))
    player_left_3 = load_image(resource_path(os.path.join('images', 'sprites', 'player', 'Left_3.png')))
    
    player_down_1 = load_image(resource_path(os.path.join('images', 'sprites', 'player', 'Down_1.png')))
    player_down_2 = load_image(resource_path(os.path.join('images', 'sprites', 'player', 'Down_2.png')))
    player_down_3 = load_image(resource_path(os.path.join('images', 'sprites', 'player', 'Down_3.png')))
    
    player_up_1 = load_image(resource_path(os.path.join('images', 'sprites', 'player', 'Up_1.png')))
    player_up_2 = load_image(resource_path(os.path.join('images', 'sprites', 'player', 'Up_2.png')))
    player_up_3 = load_image(resource_path(os.path.join('images', 'sprites', 'player', 'Up_3.png')))
    
    player_animation = {
        'stay': player_stay,
        'right': [player_right_1, player_right_2, player_right_3, player_right_2, player_right_1],
        'left': [player_left_1, player_left_2, player_left_3, player_left_2, player_left_1],
        'down': [player_down_1, player_down_2, player_down_3, player_down_2, player_down_1],
        'up': [player_up_1, player_up_2, player_up_3, player_up_2, player_up_1]
    }
    
    blinky_right_1 = load_image_black_bg(resource_path(os.path.join('images', 'sprites', 'enemy', 'blinky', 'Right_1.png')))
    blinky_right_2 = load_image_black_bg(resource_path(os.path.join('images', 'sprites', 'enemy', 'blinky', 'Right_2.png')))
    
    blinky_left_1 = load_image_black_bg(resource_path(os.path.join('images', 'sprites', 'enemy', 'blinky', 'Left_1.png')))
    blinky_left_2 = load_image_black_bg(resource_path(os.path.join('images', 'sprites', 'enemy', 'blinky', 'Left_2.png')))
    
    blinky_down_1 = load_image_black_bg(resource_path(os.path.join('images', 'sprites', 'enemy', 'blinky', 'Down_1.png')))
    blinky_down_2 = load_image_black_bg(resource_path(os.path.join('images', 'sprites', 'enemy', 'blinky', 'Down_2.png')))
    
    blinky_up_1 = load_image_black_bg(resource_path(os.path.join('images', 'sprites', 'enemy', 'blinky', 'Up_1.png')))
    blinky_up_2 = load_image_black_bg(resource_path(os.path.join('images', 'sprites', 'enemy', 'blinky', 'Up_2.png')))
    
    clyde_right_1 = load_image_black_bg(resource_path(os.path.join('images', 'sprites', 'enemy', 'clyde', 'Right_1.png')))
    clyde_right_2 = load_image_black_bg(resource_path(os.path.join('images', 'sprites', 'enemy', 'clyde', 'Right_2.png')))
    
    clyde_left_1 = load_image_black_bg(resource_path(os.path.join('images', 'sprites', 'enemy', 'clyde', 'Left_1.png')))
    clyde_left_2 = load_image_black_bg(resource_path(os.path.join('images', 'sprites', 'enemy', 'clyde', 'Left_2.png')))
    
    clyde_down_1 = load_image_black_bg(resource_path(os.path.join('images', 'sprites', 'enemy', 'clyde', 'Down_1.png')))
    clyde_down_2 = load_image_black_bg(resource_path(os.path.join('images', 'sprites', 'enemy', 'clyde', 'Down_2.png')))
    
    clyde_up_1 = load_image_black_bg(resource_path(os.path.join('images', 'sprites', 'enemy', 'clyde', 'Up_1.png')))
    clyde_up_2 = load_image_black_bg(resource_path(os.path.join('images', 'sprites', 'enemy', 'clyde', 'Up_2.png')))
    
    inky_right_1 = load_image_black_bg(resource_path(os.path.join('images', 'sprites', 'enemy', 'inky', 'Right_1.png')))
    inky_right_2 = load_image_black_bg(resource_path(os.path.join('images', 'sprites', 'enemy', 'inky', 'Right_2.png')))
    
    inky_left_1 = load_image_black_bg(resource_path(os.path.join('images', 'sprites', 'enemy', 'inky', 'Left_1.png')))
    inky_left_2 = load_image_black_bg(resource_path(os.path.join('images', 'sprites', 'enemy', 'inky', 'Left_2.png')))
    
    inky_down_1 = load_image_black_bg(resource_path(os.path.join('images', 'sprites', 'enemy', 'inky', 'Down_1.png')))
    inky_down_2 = load_image_black_bg(resource_path(os.path.join('images', 'sprites', 'enemy', 'inky', 'Down_2.png')))
    
    inky_up_1 = load_image_black_bg(resource_path(os.path.join('images', 'sprites', 'enemy', 'inky', 'Up_1.png')))
    inky_up_2 = load_image_black_bg(resource_path(os.path.join('images', 'sprites', 'enemy', 'inky', 'Up_2.png')))
    
    pinky_right_1 = load_image_black_bg(resource_path(os.path.join('images', 'sprites', 'enemy', 'pinky', 'Right_1.png')))
    pinky_right_2 = load_image_black_bg(resource_path(os.path.join('images', 'sprites', 'enemy', 'pinky', 'Right_2.png')))
    
    pinky_left_1 = load_image_black_bg(resource_path(os.path.join('images', 'sprites', 'enemy', 'pinky', 'Left_1.png')))
    pinky_left_2 = load_image_black_bg(resource_path(os.path.join('images', 'sprites', 'enemy', 'pinky', 'Left_2.png')))
    
    pinky_down_1 = load_image_black_bg(resource_path(os.path.join('images', 'sprites', 'enemy', 'pinky', 'Down_1.png')))
    pinky_down_2 = load_image_black_bg(resource_path(os.path.join('images', 'sprites', 'enemy', 'pinky', 'Down_2.png')))
    
    pinky_up_1 = load_image_black_bg(resource_path(os.path.join('images', 'sprites', 'enemy', 'pinky', 'Up_1.png')))
    pinky_up_2 = load_image_black_bg(resource_path(os.path.join('images', 'sprites', 'enemy', 'pinky', 'Up_2.png')))
    
    enemies_animation = {
        'blinky': {
            'right': [blinky_right_1, blinky_right_2],
            'left': [blinky_left_1, blinky_left_2],
            'down': [blinky_down_1, blinky_down_2],
            'up': [blinky_up_1, blinky_up_2]
        },
        'clyde': {
            'right': [clyde_right_1, clyde_right_2],
            'left': [clyde_left_1, clyde_left_2],
            'down': [clyde_down_1, clyde_down_2],
            'up': [clyde_up_1, clyde_up_2]
        },
        'inky': {
            'right': [inky_right_1, inky_right_2],
            'left': [inky_left_1, inky_left_2],
            'down': [inky_down_1, inky_down_2],
            'up': [inky_up_1, inky_up_2]
        },
        'pinky': {
            'right': [pinky_right_1, pinky_right_2],
            'left': [pinky_left_1, pinky_left_2],
            'down': [pinky_down_1, pinky_down_2],
            'up': [pinky_up_1, pinky_up_2]
        }
    }