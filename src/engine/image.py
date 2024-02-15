import pygame

class Image:
    background = pygame.image.load('./images/testbg.png')
    block_cell = pygame.image.load('./images/sprites/BlockCell.png')
    empty_cell = pygame.image.load('./images/sprites/EmptyCell.png')
    food_cell = pygame.image.load('./images/sprites/FoodCell.png')
    player_stay = pygame.image.load('./images/sprites/player/Stay.png')
    player_stay.set_colorkey((255, 255, 255))