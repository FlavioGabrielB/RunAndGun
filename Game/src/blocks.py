import pygame

class Blocks(pygame.sprite.Sprite):
    def __init__(self, size, type=0, pos=(0,0)):
        super().__init__()
        self.type = type

        self.sprite = pygame.image.load('imgs/blocks/pixil-frame-0.png').convert_alpha()

        if(type == 0):
            self.sprite = pygame.image.load('imgs/blocks/pixil-frame-0.png').convert_alpha()
        elif(type == 1):
            self.sprite = pygame.image.load('imgs/blocks/pixil-frame-1.png').convert_alpha()
        

        self.image = pygame.transform.scale(self.sprite, (size, size))
        self.rect = self.image.get_rect(topleft = pos)