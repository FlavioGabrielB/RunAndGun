import pygame
import math
class static_bullet(pygame.sprite.Sprite):
    def __init__(self, player_pos, angle):
        super().__init__()
        self.sprite_bullet = [pygame.image.load('imgs/bullet/pixil-frame-0.png').convert_alpha(), pygame.image.load('imgs/bullet/pixil-frame-1.png').convert_alpha(),
                                 pygame.image.load('imgs/bullet/pixil-frame-2.png').convert_alpha(), pygame.image.load('imgs/bullet/pixil-frame-3.png').convert_alpha()]
        self.image = self.sprite_bullet[0]
        self.bullet_pos = pygame.math.Vector2(player_pos[0], player_pos[1])
        self.switch_time = 1000
        self.dt = 0
        self.size = 70
        self.angle = angle
        self.angle_rad = math.radians(angle)
        self.pos_x = math.cos(self.angle_rad) 
        self.pos_y = math.sin(self.angle_rad) 
        self.pos_x *= self.size
        self.pos_y *= self.size
        self.hitbox = (40, 40)
        self.rect = pygame.Rect(self.bullet_pos, self.hitbox)
        self.rediret_hitbox = -7

        self.dt_switch_sprite = 0
        self.switch_time_sprite = 100
        self.index_frame = 0

    def switch_sprite(self):
        time = pygame.time.get_ticks()
        if(time - self.dt_switch_sprite > self.switch_time_sprite):
                self.index_frame = (self.index_frame + 1) % len(self.sprite_bullet)
                self.dt_switch_sprite = time
        self.image = self.sprite_bullet[self.index_frame]

    def bullet_static_rotation(self, angle, player_pos):
        #self.image = pygame.transform.rotate(self.image_static_original, angle - 90)
        self.switch_sprite()
        self.angle_rad = math.radians(-angle)
        self.pos_x = math.cos(self.angle_rad) 
        self.pos_y = math.sin(self.angle_rad) 
        self.pos_x *= self.size
        self.pos_y *= self.size
        self.bullet_pos = pygame.math.Vector2(player_pos[0]+self.pos_x, player_pos[1]+self.pos_y)
        self.rect = pygame.Rect(self.bullet_pos.x - 20 , self.bullet_pos.y -20, self.hitbox[0], self.hitbox[1])

       