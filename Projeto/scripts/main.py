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
enemy = Base_enemy(width_screen, height, 0)
grupo_enemy = pygame.sprite.Group(enemy)
grupo_bullet = pygame.sprite.Group()
all_sprites_group = pygame.sprite.Group()
all_sprites_group.add(enemy)

while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    dt = clock.tick(60) / 100

    screen.blit(fundo, (0, 0))

    all_sprites_group.update()

    all_sprites_group.draw(fundo)

    # all_sprites_group.draw(screen)

    # all_sprites_group.update()

    pygame.display.flip()    
    
pygame.quit()