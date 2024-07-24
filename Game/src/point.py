import pygame
import math

class Point(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.sprite = pygame.image.load('imgs/blocks/pixil-frame-1.png').convert_alpha()
        self.image = pygame.transform.scale(self.sprite, (50,50))
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 400
        self.velocity = 10
        self.const = 120


        self.pos_y = 400
        self.pos_x = 400

    def move(self, player):
        # self.rect.x = player.x
        # self.rect.y = player.y

        
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.pos_x = player.x + self.const
            self.pos_y = player.y
        if keys[pygame.K_a]:
           self.pos_x = player.x - self.const
           self.pos_y = player.y
        if keys[pygame.K_w]:
            self.pos_y = player.y - self.const
            self.pos_x = player.x
        if keys[pygame.K_s]:
            self.pos_y = player.y + self.const
            self.pos_x = player.x
        
        self.rect.x = self.pos_x
        self.rect.y = self.pos_y
        
            
