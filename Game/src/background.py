import pygame

class Background(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.sprite = [pygame.image.load('imgs/background/pixil-frame-0.png').convert_alpha(), pygame.image.load('imgs/background/pixil-frame-1.png').convert_alpha(),
                       pygame.image.load('imgs/background/pixil-frame-2.png').convert_alpha(), pygame.image.load('imgs/background/pixil-frame-3.png').convert_alpha()]
        
        self.image = self.sprite[3] 
        self.rect = self.image.get_rect()

        self.dt_switch_sprite = 0
        self.switch_time_sprite = 100
        self.index_frame = 0
    
    def switch_sprite(self):
        time = pygame.time.get_ticks()
        if(time - self.dt_switch_sprite > self.switch_time_sprite):
                self.index_frame = (self.index_frame + 1) % len(self.sprite)
                self.dt_switch_sprite = time
        self.image = self.sprite[self.index_frame]