import pygame

def load_image(image_name):
    result = pygame.image.load(image_name)
    result.set_colorkey((255, 255, 255))
    return result 

#TODO: Image -> Spirtes
class Image:
    background = pygame.image.load('./images/testbg.png')
    block_cell = pygame.image.load('./images/sprites/BlockCell.png')
    empty_cell = pygame.image.load('./images/sprites/EmptyCell.png')
    food_cell = pygame.image.load('./images/sprites/FoodCell.png')
    
    health_point = load_image('./images/sprites/HP.png')
    health_point = pygame.transform.scale(health_point, (50, 50))
    
    player_stay = load_image('./images/sprites/player/Stay.png')
    
    player_right_1 = load_image('./images/sprites/player/Right_1.png')
    player_right_2 = load_image('./images/sprites/player/Right_2.png')
    player_right_3 = load_image('./images/sprites/player/Right_3.png')
    
    player_left_1 = load_image('./images/sprites/player/Left_1.png')
    player_left_2 = load_image('./images/sprites/player/Left_2.png')
    player_left_3 = load_image('./images/sprites/player/Left_3.png')
    
    player_down_1 = load_image('./images/sprites/player/Down_1.png')
    player_down_2 = load_image('./images/sprites/player/Down_2.png')
    player_down_3 = load_image('./images/sprites/player/Down_3.png')
    
    player_up_1 = load_image('./images/sprites/player/Up_1.png')
    player_up_2 = load_image('./images/sprites/player/Up_2.png')
    player_up_3 = load_image('./images/sprites/player/Up_3.png')