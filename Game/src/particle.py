import pygame
import random
class Particle(pygame.sprite.Sprite):
    def __init__(self, pos, color, tam=5):
        super().__init__()
        self.size = (tam, tam)
        self.images = [pygame.image.load('imgs/explison-particles/pixil-frame-1.png').convert_alpha(), pygame.image.load('imgs/explison-particles/pixil-frame-2.png').convert_alpha(),
                       pygame.image.load('imgs/explison-particles/pixil-frame-2.png').convert_alpha(), pygame.image.load('imgs/explison-particles/pixil-frame-3.png').convert_alpha()]
        
        self.images_1 = [pygame.image.load('imgs/explison-particles/pixil-frame-0.png').convert_alpha(), pygame.image.load('imgs/explison-particles/pixil-frame-2.png').convert_alpha(),
                       pygame.image.load('imgs/explison-particles/pixil-frame-0.png').convert_alpha(), pygame.image.load('imgs/explison-particles/pixil-frame-0.png').convert_alpha()]
        
        self.images_2 = [pygame.image.load('imgs/explison-particles/pixil-frame-0.png').convert_alpha(), pygame.image.load('imgs/explison-particles/pixil-frame-4.png').convert_alpha(),
                       pygame.image.load('imgs/explison-particles/pixil-frame-0.png').convert_alpha(), pygame.image.load('imgs/explison-particles/pixil-frame-4.png').convert_alpha()]

        self.image = pygame.image.load('imgs/explison-particles/pixil-frame-0.png').convert_alpha()
        self.pos = []
        self.pos.append(pos[0])
        self.pos.append(pos[1])
        self.pos[0] += random.randint(1, 30) + 30
        self.pos[1] += random.randint(1, 30) + 20
        self.rect = self.image.get_rect(center=self.pos)
        self.color = color
        self.dt_swap_image = 0
        self.index_frame_1 = 0
        self.index_frame = 0

        while True:
            self.velocty_x = random.randint(-1, 1)
            self.velocty_y = random.randint(-1, 1)
            if(self.velocty_x != 0 or self.velocty_y != 0):
                break

    def animation_1(self):

        time = pygame.time.get_ticks()

        if(time - self.dt_swap_image > 200):
            self.index_frame_1 = (self.index_frame_1 + 1) % len(self.images)
            self.dt_swap_image = time

        self.image = pygame.transform.scale(self.images[self.index_frame_1], self.size)

        #self.image = self.images[self.index_frame_1]

        self.rect.x += self.velocty_x
        self.rect.y += self.velocty_y

    def animation_boost(self):

        time = pygame.time.get_ticks()

        if(time - self.dt_swap_image > 200):
            self.index_frame_1 = (self.index_frame_1 + 1) % len(self.images_2)
            self.dt_swap_image = time

        self.image = pygame.transform.scale(self.images_2[self.index_frame_1], self.size)

        #self.image = self.images_2[self.index_frame_1]
        self.rect.x += self.velocty_x*1.5
        self.rect.y += self.velocty_y*1.5

    def animation_2(self, x):
        time = pygame.time.get_ticks()

        if(time - self.dt_swap_image > 50):
            self.index_frame = (self.index_frame + 1) % len(self.images)
            self.dt_swap_image = time

        self.image = pygame.transform.scale(self.images_1[self.index_frame], self.size)
        #self.image = self.images_1[self.index_frame]
        self.rect.x += self.velocty_x*x
        self.rect.y += self.velocty_y*x

