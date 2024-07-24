import pygame
from src import Game

pygame.init()

screen = pygame.display.set_mode((1280, 640))
clock = pygame.time.Clock()
running = True
dt = 0
Game_ = Game.Game(screen)

back = (40, 11, 38)

font = pygame.font.Font(None, 36)  

rect = screen.get_rect()

LB = False


while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        

    text = f"{int(clock.get_fps())}"
    text_surface = font.render(text, True, "WHITE")
    Game_.update()
    screen.fill(back)        
    Game_.draw()
    screen.blit(text_surface, (1253, 0))
    pygame.display.flip()
    dt = clock.tick(60) 
