import pygame
import math
from src import range
class tower(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.image_original = pygame.image.load('imgs/bullet/pixil-frame-0.png').convert_alpha()
        self.image = pygame.image.load('imgs/bullet/pixil-frame-0.png').convert_alpha()
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.rect = self.image.get_rect(center = (self.pos_x, self.pos_y))
        self.bullets = []
        self.range = range.range(self.pos_x, self.pos_y)
        self.dt_bullet = 0
        
    def rotation(self, enemy_pos_x, enemy_pos_y):
        dif_x =  enemy_pos_x - self.pos_x
        dif_y = -(enemy_pos_y - self.pos_y)

        self.angle = math.degrees(math.atan2(dif_y, dif_x))

        self.image = pygame.transform.rotate(self.image_original, self.angle - 90)
        self.rect = self.image.get_rect(center = (self.pos_x, self.pos_y))
        

    