import pygame

class Heart(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.sprites = [pygame.transform.scale(pygame.image.load('imgs/heart/pixil-frame-0.png').convert_alpha(), (84,84)),pygame.transform.scale(pygame.image.load('imgs/heart/pixil-frame-1.png').convert_alpha(), (64,64)),
                        pygame.transform.scale(pygame.image.load('imgs/heart/pixil-frame-2.png').convert_alpha(), (64,64)), pygame.transform.scale(pygame.image.load('imgs/heart/pixil-frame-3.png').convert_alpha(), (64,64))]
        self.image = self.sprites[0]
        self.pos = pygame.math.Vector2(0,0)
        self.rect = self.image.get_rect()
        self.dt = 0
        self.index_frame = 0

    def animation(self):
        time = pygame.time.get_ticks()
        if (time - self.dt > 100):
            self.index_frame = (self.index_frame + 1) % len(self.sprites)
            self.dt = time
        self.image = self.sprites[self.index_frame]
        self.rect = self.image.get_rect(center = self.pos)