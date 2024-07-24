import pygame
import math
class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, screen):
        super().__init__()
        self.original_image = pygame.image.load("imgs/enemy/pixil-frame-0.png").convert_alpha()
        
        self.images = [pygame.image.load("imgs/enemy/pixil-frame-0.png").convert_alpha(), pygame.image.load("imgs/enemy/pixil-frame-1.png").convert_alpha(),
                       pygame.image.load("imgs/enemy/pixil-frame-2.png").convert_alpha(), pygame.image.load("imgs/enemy/pixil-frame-3.png").convert_alpha()]

        self.rediret_hitbox = 0
        self.life = 1  
        self.x = x
        self.y = y
        self.hitbox = (60, 60)
        self.enemy_pos = pygame.math.Vector2(x, y)
        self.velocity = 5
        self.rect = pygame.Rect(self.enemy_pos.x, self.enemy_pos.y, self.hitbox[0], self.hitbox[1])
        self.screen = screen
        self.image = []
        self.dt_swap_image = 0
        self.index_frame = 0
        self.time = pygame.time.get_ticks()

    def rotation(self, pos_player_x, pos_player_y):

        time = pygame.time.get_ticks()

        if(time - self.dt_swap_image > 100):
            self.index_frame = (self.index_frame + 1) % len(self.images)
            self.dt_swap_image = time

        dif_x =  pos_player_x - self.enemy_pos.x
        dif_y = -(pos_player_y - self.enemy_pos.y)

        self.angle = math.degrees(math.atan2(dif_y, dif_x))

        self.image = pygame.transform.rotate(self.images[self.index_frame], self.angle - 90)
        self.rect = self.image.get_rect(center = self.enemy_pos)
        
        self.rect.height = 90
        self.rect.width = 90
        self.dt_time_attack = 0
        

    def move(self, pos_player_x, pos_player_y, enemys):
        self.d_x = pos_player_x - self.enemy_pos.x 
        self.d_y = pos_player_y - self.enemy_pos.y 

        self.module = math.sqrt(self.d_x*self.d_x + self.d_y*self.d_y)

        self.d_x = self.d_x / self.module * self.velocity 
        self.d_y = self.d_y / self.module * self.velocity

        self.enemy_pos += pygame.math.Vector2(self.d_x, self.d_y)
        if(len(enemys) > 0):
            for enemy in enemys:
                d_x = self.rect.x - enemy.rect.x
                d_y = self.rect.y - enemy.rect.y
                if enemy != self and self.rect.colliderect(enemy.rect) and (d_x > 0 or d_y > 0) :
                    move_direction = pygame.math.Vector2(d_x, d_y).normalize()
                    self.enemy_pos += pygame.math.Vector2(move_direction.x*self.velocity, move_direction.y*self.velocity)

        self.rotation(pos_player_x, pos_player_y)
        
        