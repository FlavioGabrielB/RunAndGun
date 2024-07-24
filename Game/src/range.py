import pygame
import math
class range(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.image = self.sprite = pygame.image.load('imgs/blocks/pixil-frame-1.png').convert_alpha()
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.range = [10000, 10000]
        self.rect = pygame.Rect(pos_x-self.range[0]/2, pos_y-self.range[1]/2, self.range[0], self.range[1])
    
        

    