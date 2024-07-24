import pygame
import math
class Hero(pygame.sprite.Sprite):
    def __init__(self, screen):
        super().__init__()

        self.screen = screen


        self.sprite_hero_walk_r = [pygame.image.load('imgs/hero-walk/pixil-frame-0.png').convert_alpha(), pygame.image.load('imgs/hero-walk/pixil-frame-1.png').convert_alpha(),
                                 pygame.image.load('imgs/hero-walk/pixil-frame-2.png').convert_alpha(), pygame.image.load('imgs/hero-walk/pixil-frame-3.png').convert_alpha()]
        
        self.sprite_hero_walk_l = [pygame.image.load('imgs/hero-walk/pixil-frame-4.png').convert_alpha(), pygame.image.load('imgs/hero-walk/pixil-frame-5.png').convert_alpha(),
                                 pygame.image.load('imgs/hero-walk/pixil-frame-6.png').convert_alpha(), pygame.image.load('imgs/hero-walk/pixil-frame-7.png').convert_alpha()]
        
        self.sprite_hero_stop = [pygame.image.load('imgs/hero-walk/pixil-frame-8.png').convert_alpha(), pygame.image.load('imgs/hero-walk/pixil-frame-9.png').convert_alpha(),
                                 pygame.image.load('imgs/hero-walk/pixil-frame-10.png').convert_alpha(), pygame.image.load('imgs/hero-walk/pixil-frame-8.png').convert_alpha()]
        
        self.sprite_hero_front = [pygame.image.load('imgs/hero-walk/pixil-frame-12.png').convert_alpha(), pygame.image.load('imgs/hero-walk/pixil-frame-13.png').convert_alpha(),
                                 pygame.image.load('imgs/hero-walk/pixil-frame-14.png').convert_alpha(), pygame.image.load('imgs/hero-walk/pixil-frame-15.png').convert_alpha()]
        
        self.player_pos = pygame.math.Vector2(1280, 1280)

        self.index_status_animation = 1

        self.image = self.sprite_hero_walk_r[0]
        self.rect = self.image.get_rect()
        self.angle = 0
        self.index_frame = 0
        self.velocity = 7
        self.velocity_boost = 30
        self.bullet_index = 0
        self.dt_sprite_player = 0
        self.dt_boost_time = 0
        self.boost_time = 1000
        self.act_boost = True
        self.switch_time_sprite = 100
        self.life = 6
        self.in_boost = False
        self.clicked_boost = False
        self.psn_btn = False
        self.hitbox_size = (50, 50)
        

    def sprite_move(self, index):
        time = pygame.time.get_ticks()
        if(index == 1):
            if(time - self.dt_sprite_player > self.switch_time_sprite):
                self.index_frame = (self.index_frame + 1) % len(self.sprite_hero_walk_r)
                self.dt_sprite_player = time
            self.image = self.sprite_hero_walk_r[self.index_frame]
        elif(index == 2):
            if(time - self.dt_sprite_player > self.switch_time_sprite):
                self.index_frame = (self.index_frame + 1) % len(self.sprite_hero_walk_l)
                self.dt_sprite_player = time
            self.image = self.sprite_hero_walk_l[self.index_frame]
        elif(index == 3):
            if(time - self.dt_sprite_player > self.switch_time_sprite):
                self.index_frame = (self.index_frame + 1) % len(self.sprite_hero_stop)
                self.dt_sprite_player = time
            self.image = self.sprite_hero_front[self.index_frame]
        else:
            if(time - self.dt_sprite_player > self.switch_time_sprite):
                self.index_frame = (self.index_frame + 1) % len(self.sprite_hero_stop)
                self.dt_sprite_player = time
            self.image = self.sprite_hero_stop[self.index_frame]

    def move(self):
        self.velocity_x = 0
        self.velocity_y = 0

        self.index_status_animation = 4

        keys = pygame.key.get_pressed()

        time = pygame.time.get_ticks()
        self.in_boost = False

        act_btn = False

        if(time - self.dt_boost_time> self.boost_time) and not self.act_boost:
            self.act_boost = True
            self.dt_boost_time = time

        if keys[pygame.K_w]:
            self.velocity_y = -self.velocity 

            if keys[pygame.K_SPACE]:
                act_btn = True
                if self.act_boost and not self.clicked_boost:
                    self.act_boost = False 
                    self.velocity_y = -self.velocity * self.velocity_boost
                    self.in_boost = True
                    self.psn_btn = True
            self.index_status_animation = 3
        if keys[pygame.K_s]:
            self.velocity_y = self.velocity 

            if keys[pygame.K_SPACE]:
                act_btn = True
                if self.act_boost and not self.clicked_boost:
                    self.act_boost = False 
                    self.velocity_y = self.velocity * self.velocity_boost 
                    self.in_boost = True
                    self.psn_btn = True
            self.index_status_animation = 3

        if keys[pygame.K_a]:
            self.velocity_x = -self.velocity
            self.index_status_animation = 2

            if keys[pygame.K_SPACE]: 
                act_btn = True
                if self.act_boost and not self.clicked_boost:
                    self.act_boost = False 
                    self.velocity_x = -self.velocity * self.velocity_boost
                    self.in_boost = True
                    self.psn_btn = True

        if keys[pygame.K_d]:
            self.velocity_x = self.velocity
            self.index_status_animation = 1 

            if keys[pygame.K_SPACE]: 
                act_btn = True
                if self.act_boost and not self.clicked_boost:
                    self.act_boost = False 
                    self.velocity_x = self.velocity * self.velocity_boost 
                    self.in_boost = True
                    self.psn_btn = True

        if(keys[pygame.K_SPACE] and self.psn_btn):
            act_btn = True

        if self.velocity_x != 0 and self.velocity_y != 0:
            self.velocity_x /= math.sqrt(2)
            self.velocity_y /= math.sqrt(2)

        self.sprite_move(self.index_status_animation)
        self.player_pos += pygame.math.Vector2(self.velocity_x, self.velocity_y)
        
        self.hitbox = pygame.Rect(self.player_pos.x-25, self.player_pos.y-25, self.hitbox_size[0],self.hitbox_size[1])

        self.clicked_boost = act_btn
        
    def rotation(self):
        mouse_pos = pygame.mouse.get_pos()

        dif_x = mouse_pos[0] - 1280/2
        dif_y = -(mouse_pos[1] - 640/2)

        self.angle = math.degrees(math.atan2(dif_y, dif_x))

    def update(self):
        self.rect = self.image.get_rect(center = self.player_pos)
        self.move()
        self.rotation()  
      