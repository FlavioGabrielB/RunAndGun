import pygame
from . import blocks

class Tilemap(pygame.sprite.Sprite):
    def __init__(self, width, height, size):
        super().__init__()
        self.initial_pos = (100,100)
        self.width = width
        self.height = height
        self.size = size
        self.invisible_blocks = []
        self.center_block_number = int((self.width*self.height)/2)
        self.center_block_index = []
        self.rect = pygame.Rect(self.initial_pos[0],self.initial_pos[1], self.width*self.size, self.height*self.size)

    def construct(self, matriz, camera, layer=0):
        num = 0
        for i in range(self.height):
            for j in range(self.width):
                if matriz[i][j] == 1:
                    block = blocks.Blocks(self.size, matriz[i][j], (i*self.size+self.initial_pos[0], j*self.size+self.initial_pos[0]))
                    self.invisible_blocks.append(block)
                else:
                    block = blocks.Blocks(self.size, matriz[i][j], (i*self.size+self.initial_pos[0], j*self.size+self.initial_pos[0]))
                camera.all_sprites.add(block, layer = layer)
        
                if num == self.center_block_number:
                    self.center_block_index.append((i*self.size+self.initial_pos[0], j*self.size+self.initial_pos[0]))
                num += 1
