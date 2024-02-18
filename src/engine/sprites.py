import pygame

class Image:
    background = pygame.image.load('./images/testbg.png')
    block_cell = pygame.image.load('./images/sprites/BlockCell.png')
    empty_cell = pygame.image.load('./images/sprites/EmptyCell.png')
    food_cell = pygame.image.load('./images/sprites/FoodCell.png')
    
    health_point = pygame.image.load('./images/sprites/HP.png')
    health_point.set_colorkey((255, 255, 255))
    health_point = pygame.transform.scale(health_point, (50, 50))
    
    player_stay = pygame.image.load('./images/sprites/player/Stay.png')
    player_stay.set_colorkey((255, 255, 255))
    
    player_right_1 = pygame.image.load('./images/sprites/player/Right_1.png')
    player_right_1.set_colorkey((255, 255, 255))
    player_right_2 = pygame.image.load('./images/sprites/player/Right_2.png')
    player_right_2.set_colorkey((255, 255, 255))
    player_right_3 = pygame.image.load('./images/sprites/player/Right_3.png')
    player_right_3.set_colorkey((255, 255, 255))
    
    player_left_1 = pygame.image.load('./images/sprites/player/Left_1.png')
    player_left_1.set_colorkey((255, 255, 255))
    player_left_2 = pygame.image.load('./images/sprites/player/Left_2.png')
    player_left_2.set_colorkey((255, 255, 255))
    player_left_3 = pygame.image.load('./images/sprites/player/Left_3.png')
    player_left_3.set_colorkey((255, 255, 255))
    
    player_down_1 = pygame.image.load('./images/sprites/player/Down_1.png')
    player_down_1.set_colorkey((255, 255, 255))
    player_down_2 = pygame.image.load('./images/sprites/player/Down_2.png')
    player_down_2.set_colorkey((255, 255, 255))
    player_down_3 = pygame.image.load('./images/sprites/player/Down_3.png')
    player_down_3.set_colorkey((255, 255, 255))
    
    player_up_1 = pygame.image.load('./images/sprites/player/Up_1.png')
    player_up_1.set_colorkey((255, 255, 255))
    player_up_2 = pygame.image.load('./images/sprites/player/Up_2.png')
    player_up_2.set_colorkey((255, 255, 255))
    player_up_3 = pygame.image.load('./images/sprites/player/Up_3.png')
    player_up_3.set_colorkey((255, 255, 255))