import pygame
import math
from random import randint
from src import Bullet
from src import Enemy
from src import Hero
from src import camera
from src import background
from src import static_bullet
from src import particle
from src import tilemap
from src import point
from src import heart
from src import tower

class Game():
    def __init__(self, screen):
        self.screen = screen 

        self.particule_time_delete_explosion = 125
        self.particule_time_delete = 50
        self.swap_time_bullet = 400
        self.delete_time_bullet = 1000
        self.bullet_destroy_time = 1000
        self.bullet_destroy_time_scene = 1000
        self.bullet_destroy_time_counter = 0

        self.static_bullet_remove = False
        self.explosion_colision_update_act = False
        self.in_animation_boost = False

        self.dt_particule_time_delete_explosion = 0
        self.dt_particule_time_delete = 0
        self.dt_bullet = 0
        self.dt_bullet_swap = 0
        self.dt_bullet_destroy_by_time = 0
        self.dt_bullet_destroy = 0
        self.dt_particule_time_delete_particle_boost = 0
        self.dt_particule_time_delete_particle_boost_2 = 0

        self.enemy_spawn_time = 3000
        self.dt_spawn_enemy = 0

        self.dt_enemy_attack = 1000

        self.temp_shot_update = True

        self.bullets = []
        self.enemys_collided = []
        self.enemys_collided_shot = []
        self.enemys = []
        self.particles_static = []
        self.particles_explosion = []

        self.hearts = []
        self.particles_boost = []
        self.stalker_particles_boost = []

        self.towers = []
        self.dt_bullet_tower_swap = 0

        self.i_particle_boost = 0
        self.i_particle_boost_2 = 0

        self.dt_inertia = 0
        self.in_inertia = False

        self.player = Hero.Hero(self.screen)
        self.background = background.Background()
        self.point = point.Point()
        self.static_bullet = static_bullet.static_bullet(self.player.player_pos, self.player.angle)
        self.camera = camera.camera(self.player, self.screen, self.background.image)
        self.camera.all_sprites.add(self.player, layer = 2)
        self.camera.all_sprites.add(self.static_bullet, layer=5)
        self.camera.all_sprites.add(self.point, layer=10)
        self.i_pos_x=0
        self.i_pos_y=0
        self.i_p_pos_x = 0
        self.i_p_pos_y = 0

        self.matriz = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                       [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
        
        self.tilemap = tilemap.Tilemap(20, 20, 128)
        self.tilemap.construct(self.matriz, self.camera, 0)
        
        for i in range(self.player.life):
            self.hearts.append(heart.Heart())

        for i in range(10):
            self.particles_boost.append(particle.Particle((self.player.rect.x, self.player.rect.y), "black", 80))
            self.stalker_particles_boost.append(particle.Particle((self.player.rect.x, self.player.rect.y), "black", 40))

    def shot_update(self):
        time = pygame.time.get_ticks()
        LB = pygame.mouse.get_pressed()[0]

        if(LB):
            if(time - self.dt_bullet_swap > self.swap_time_bullet):
                self.bullets.append(Bullet.Bullet(self.player.player_pos, -self.player.angle, self.static_bullet.bullet_pos))
                self.dt_bullet_swap = time
            self.bullet_destroy_time_counter = 0

        if(len(self.bullets) > 0):
            for bullet in self.bullets:
                bullet.move(self.screen)
                self.camera.all_sprites.add(bullet, layer = 3)

                bullet.particles.append(particle.Particle((bullet.rect.x, bullet.rect.y), "red", 7))
                
                for particule in bullet.particles:
                    particule.animation_1()
                    self.camera.all_sprites.add(particule, layer=8)
                
                if(time - bullet.dt_particle_delete> self.particule_time_delete and len(bullet.particles) > 20):
                    for i in range(5):
                        self.camera.all_sprites.remove(bullet.particles[i])
                    bullet.particles = bullet.particles[5:]
                    bullet.dt_particle_delete = time

            if(len(self.bullets) > 5):
                self.camera.all_sprites.remove(self.bullets[0])
                for particule in self.bullets[0].particles:
                    self.camera.all_sprites.remove(particule)
                self.bullets = self.bullets[1:]

            if(not LB):
                if(time - self.dt_bullet_destroy_by_time > self.bullet_destroy_time):
                    self.bullet_destroy_time_counter += 1
                    self.dt_bullet_destroy_by_time = time
                if(self.bullet_destroy_time_counter >= 3):
                    for bullet in self.bullets:
                        for particule in bullet.particles:
                            self.camera.all_sprites.remove(particule)
                        self.camera.all_sprites.remove(bullet)
                        bullet.particles.clear()
                    self.bullets.clear()
                    self.bullet_destroy_time_counter = 0
        
    def tower_update(self):
        keys = pygame.key.get_pressed()
        time = pygame.time.get_ticks()

        if keys[pygame.K_e]:
            self.towers.append(tower.tower(self.player.player_pos.x, self.player.player_pos.y))
        
        if(len(self.towers)>0):
            for towe in self.towers:
                tower_collided = pygame.sprite.spritecollide(towe.range, self.enemys, False)
                if(len(tower_collided)>0):
                    towe.rotation(tower_collided[0].rect.x, tower_collided[0].rect.y)

                    if(time - towe.dt_bullet > self.swap_time_bullet):
                        towe.bullets.append(Bullet.Bullet((towe.pos_x, towe.pos_y), -towe.angle, [towe.pos_x, towe.pos_y], 1))
                        towe.dt_bullet = time

                self.camera.all_sprites.add(towe, layer=10)

                if(len(towe.bullets) > 0):
                    for bullet in towe.bullets:
                        bullet.move(self.camera.screen)
                        self.camera.all_sprites.add(bullet, layer=4)

    def explosion_colision_update(self, obj=None):
        time = pygame.time.get_ticks()
        if(obj != None):
            for i in range(6):
                self.particles_explosion.append(particle.Particle((obj.rect.x, obj.rect.y), "red", 35))
            
        if(len(self.particles_explosion) > 0):
            for particule in self.particles_explosion:
                particule.animation_2(5)
                self.camera.all_sprites.add(particule, layer=9)
            self.explosion_colision_update_act = True

            if(time - self.dt_particule_time_delete_explosion > self.particule_time_delete_explosion):
                for i in range(2):
                    self.camera.all_sprites.remove(self.particles_explosion[i])
                self.particles_explosion = self.particles_explosion[2:]
                self.dt_particule_time_delete_explosion = time
                self.explosion_colision_update_act = False 
        
    def enemy_update(self):
        time = pygame.time.get_ticks()

        x = randint(100, 400)
        y = randint(100, 400)

        if(time - self.dt_spawn_enemy > self.enemy_spawn_time):
            self.enemys.append(Enemy.Enemy(x, y, self.screen))
            self.dt_spawn_enemy = time

        for enemy in self.enemys:
            self.enemys_collided = pygame.sprite.spritecollide(enemy, self.enemys, False)
            self.enemys_collided_shot = pygame.sprite.spritecollide(enemy, self.bullets, False)

            self.camera.all_sprites.add(enemy, layer=4)

            if(enemy.rect.colliderect(self.player.hitbox)):
                self.i_pos_x = enemy.enemy_pos.x
                self.i_pos_y = enemy.enemy_pos.y
                self.i_p_pos_x = self.player.player_pos.x
                self.i_p_pos_y = self.player.player_pos.y
                self.player.life -= 1

                self.in_inertia = True
                if(time-self.dt_enemy_attack > 500):

                    if(len(self.hearts) > 0):
                        self.hearts.pop()
                    self.dt_enemy_attack = time

                if(not self.in_inertia):
                    d_x = self.i_p_pos_x - self.i_pos_x
                    d_y = self.i_p_pos_y - self.i_pos_y
                    if(math.sqrt(d_x*d_x + d_y*d_y) != 0):
                        self.player.player_pos.x += d_x / math.sqrt(d_x*d_x + d_y*d_y)*5
                        self.player.player_pos.y += d_y / math.sqrt(d_x*d_x + d_y*d_y)*5

            if(time - self.dt_inertia > 300 and self.in_inertia):
                self.in_inertia = False
                self.dt_inertia = time


            if(len(self.enemys_collided_shot) > 0):
               
                self.explosion_colision_update(self.enemys_collided_shot[0])

                d_x = enemy.enemy_pos.x - self.enemys_collided_shot[0].rect.x 
                d_y = enemy.enemy_pos.y - self.enemys_collided_shot[0].rect.y 

                enemy.enemy_pos.x += d_x / math.sqrt(d_x*d_x + d_y*d_y) * 25
                enemy.enemy_pos.y += d_y / math.sqrt(d_x*d_x + d_y*d_y) * 25

                if(enemy.life == 0):
                    self.enemys.remove(enemy)
                    self.camera.all_sprites.remove(enemy)
                for particule in self.enemys_collided_shot[0].particles:
                    self.camera.all_sprites.remove(particule)
                self.enemys_collided_shot[0].particles.clear()
                self.bullets.remove(self.enemys_collided_shot[0])
                self.camera.all_sprites.remove(self.enemys_collided_shot[0])
                enemy.life-= 1
                enemy.move(self.player.player_pos.x, self.player.player_pos.y, self.enemys_collided[1:])

            else:
                enemy.move(self.player.player_pos.x, self.player.player_pos.y, self.enemys_collided[1:])

        if(self.in_inertia):
            d_x = self.i_p_pos_x - self.i_pos_x
            d_y = self.i_p_pos_y - self.i_pos_y
            if(math.sqrt(d_x*d_x + d_y*d_y) != 0):
                self.player.player_pos.x += d_x / math.sqrt(d_x*d_x + d_y*d_y)*10
                self.player.player_pos.y += d_y / math.sqrt(d_x*d_x + d_y*d_y)*10

    def static_bullet_update(self):
        time = pygame.time.get_ticks()
        if(not self.player.in_boost):
            if(self.static_bullet_remove):
                self.camera.all_sprites.add(self.static_bullet, layer=5)
            self.static_bullet.bullet_static_rotation(self.player.angle, self.player.player_pos)
        else:
            self.camera.all_sprites.remove(self.static_bullet)
            self.static_bullet_remove = True
        
        self.particles_static.append(particle.Particle((self.static_bullet.rect.x, self.static_bullet.rect.y), "black"))
       

        for particule in self.particles_static:
            particule.animation_1()
            self.camera.all_sprites.add(particule, layer=7)

        if(time - self.dt_particule_time_delete > self.particule_time_delete and len(self.particles_static) > 40):
            for i in range(5):
                self.camera.all_sprites.remove(self.particles_static[i])
            self.particles_static = self.particles_static[5:]

            self.dt_particule_time_delete = time

    def particles_in_boost(self):
        time = pygame.time.get_ticks()
        keys = pygame.key.get_pressed()


        if(self.player.in_boost):

            if keys[pygame.K_d] and keys[pygame.K_w]:
                x = -50
                y = -50
            elif keys[pygame.K_w] and keys[pygame.K_a]:
                x = 50
                y = -50
            elif keys[pygame.K_a] and keys[pygame.K_s]:
                x = 50
                y = 50
            elif keys[pygame.K_s] and keys[pygame.K_d]:
                x = -50
                y = 50
            elif keys[pygame.K_w]:
                x = 0
                y = -30
            elif keys[pygame.K_s]:
                x = 0
                y = 60
            elif keys[pygame.K_a]:
                x = -30
                y = 0
            elif keys[pygame.K_d]:
                x = 30
                y = 0
            else:
                x = 0
                y = 0
    
            self.in_animation_boost = True

            for particule in self.particles_boost:
                particule.rect.x =  self.player.rect.x + x
                particule.rect.y =  self.player.rect.y + y

                self.camera.all_sprites.add(particule, layer = 12)

            for particule in self.stalker_particles_boost:
                particule.rect.x = self.player.player_pos.x 
                particule.rect.y = self.player.player_pos.y
                self.camera.all_sprites.add(particule, layer = 12)
        
        if( self.in_animation_boost):
            for particule in self.particles_boost:
                particule.animation_boost()
            
            for particule in self.stalker_particles_boost:
                particule.animation_boost()

        if(time - self.dt_particule_time_delete_particle_boost > 35):
            self.i_particle_boost = (self.i_particle_boost + 1) % len(self.particles_boost)
            self.camera.all_sprites.remove(self.particles_boost[self.i_particle_boost])    
            self.dt_particule_time_delete_particle_boost = time

        if(time - self.dt_particule_time_delete_particle_boost_2 > 60):
            self.i_particle_boost_2 = (self.i_particle_boost_2 + 1) % len(self.stalker_particles_boost)
            self.camera.all_sprites.remove(self.stalker_particles_boost[self.i_particle_boost_2])  
            self.dt_particule_time_delete_particle_boost_2 = time
            self.in_animation_boost = True

    def player_collide(self):

        blocks_collided = pygame.sprite.spritecollide(self.player, self.tilemap.invisible_blocks, False)
        points_collided = pygame.sprite.spritecollide(self.point, self.tilemap.invisible_blocks, False)
        if(not self.tilemap.rect.colliderect(self.player.rect)):
            d_x_p =  self.tilemap.center_block_index[0][0] - self.player.rect.x 
            d_y_p =  self.tilemap.center_block_index[0][1] - self.player.rect.y 

            module = math.sqrt(d_x_p*d_x_p + d_y_p*d_y_p)

            if(module != 0):
                self.player.player_pos.x += d_x_p/module * 300
                self.player.player_pos.y += d_y_p/module * 300
                
        if(len(points_collided) > 0):
            
            self.player.act_boost = False        

        if(len(blocks_collided) > 0):
           
            self.player.act_boost = False
           
            for block_collided in blocks_collided:
                d_x =  self.player.rect.x - block_collided.rect.x 
                d_y =  self.player.rect.y - block_collided.rect.y 

                module = math.sqrt(d_x*d_x + d_y*d_y)
                if (module != 0):
                    self.player.player_pos.x += d_x/module * 7
                    self.player.player_pos.y += d_y/module * 7
                    
    def update(self):
        self.explosion_colision_update()
        self.particles_in_boost()
        self.player.update()
        self.static_bullet_update()
        self.shot_update()
        self.enemy_update()
        self.player_collide()
        self.tower_update()
        self.point.move(self.player.player_pos)

    def draw(self):
        self.camera.draw(self.explosion_colision_update_act)
        self.camera.gui(self.hearts)