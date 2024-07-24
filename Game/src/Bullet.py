import pygame
import math
class Bullet(pygame.sprite.Sprite):
    def __init__(self, player_pos, angle, static_pos, type=0, size=64):
        super().__init__()
        self.image_original = pygame.image.load('imgs/bullet/pixil-frame-0.png').convert_alpha()
        self.image = pygame.transform.scale(self.image_original, (size, size))
        self.switch_time = 1000
        self.dt = 0
        self.velocity = 15
        self.angle_rad = math.radians(angle)
        self.pos_x = math.cos(self.angle_rad) 
        self.pos_y = math.sin(self.angle_rad) 
        self.pos_x *= self.velocity
        self.pos_y *= self.velocity
        self.hitbox = (40, 40)
        if(type==0):
            self.bullet_pos = pygame.math.Vector2(static_pos.x-20, static_pos.y-20)
        else:
            self.bullet_pos = pygame.math.Vector2(static_pos[0]-20, static_pos[1]-20)
        self.rect = pygame.Rect(self.bullet_pos, self.hitbox)
        self.rediret_hitbox = -7
        self.particles = []
        self.dt_particle_delete = 0


    def move(self, screen):
        self.bullet_pos += pygame.math.Vector2(self.pos_x, self.pos_y)
        self.rect = pygame.Rect(self.bullet_pos.x , self.bullet_pos.y , self.hitbox[0], self.hitbox[1])
        
       