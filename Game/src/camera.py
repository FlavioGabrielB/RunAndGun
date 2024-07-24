import pygame
import random
class camera():
    def __init__(self, player, screen, background):
        super().__init__()
        self.screen = screen
        self.offset = pygame.math.Vector2()
        self.floor_rect = background.get_rect(topleft = (0,0))
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.player = player
        self.background = background
        self.temp_rect = None

    def gui(self, hearts):
        i = len(hearts)
        
        for heart in hearts:
            heart.pos.x = i*32
            heart.pos.y = 32
            heart.animation()
            self.screen.blit(heart.image, heart.rect)
            i-=1

    def draw(self, explosion=False):
        self.offset.x = self.player.rect.centerx - 1280 / 2
        self.offset.y = self.player.rect.centery - 640 / 2
        floor_pos = self.floor_rect.topleft - self.offset

        if explosion:
            x = random.randint(-2, 2)
            y = random.randint(-2, 2)
        else: 
            x = 0
            y = 0

        for sprite in self.all_sprites:
            
            offset_pos = sprite.rect.topleft - self.offset + (x, y)
            
            #offset_pos = sprite.rect.topleft 
            self.screen.blit(sprite.image, offset_pos)
            #pygame.draw.rect(self.screen, "red", sprite.rect, 5)
            
            
            
