import pygame
from enemy import *

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 1040))
clock = pygame.time.Clock()
running = True
colisao = False
dt = 0
fundo = pygame.image.load('Projeto/assets/fundo.png')
enemy = base_enemy(width_screen, height, 0)
grupo_enemy = pygame.sprite.Group(enemy)

while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    dt = clock.tick(60) / 100

    screen.blit(fundo, (0, 0))

    grupo_enemy.update()

    grupo_enemy.draw(fundo)

    pygame.display.flip()    
    
pygame.quit()