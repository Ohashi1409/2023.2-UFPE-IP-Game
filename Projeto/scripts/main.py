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
chao = pygame.image.load('Projeto/assets/ground.png').convert_alpha()
enemy = Base_enemy(width_screen, height, 0)
bullet = Bullet(450, 100, 45)
grupo_enemy = pygame.sprite.Group()
grupo_enemy.add(enemy)
grupo_bullet = pygame.sprite.Group()
grupo_bullet.add(bullet)
blocks = pygame.sprite.Group()
blocks.add(Ground(500, 600))
all_sprites_group = pygame.sprite.Group()
all_sprites_group.add(enemy)

while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    dt = clock.tick(60) / 100

    screen.blit(fundo, (0, 0))

    grupo_bullet.update()

    grupo_bullet.draw(screen)

    blocks.update()

    blocks.draw(screen)

    all_sprites_group.update()

    all_sprites_group.draw(screen)

    pygame.display.flip()    
    
pygame.quit()