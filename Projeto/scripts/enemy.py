#importando pygame e livraria necessaria
import pygame
from pygame.locals import *
import time
import math

pygame.init()

width_screen = 1280
width = 1050
height = 200
cont = []
shoot_cooldown = 5
bullet_scale = 1.4
bullet_speed = 10
bullet_lifetime = 500

# Criar classe de inimigo
enemy_img = pygame.image.load('Projeto/assets/R-Sheet-Sheet.png')
bullet_image = pygame.image.load('Projeto/assets/bullet.png')
bullet_image = pygame.transform.rotozoom(bullet_image, 0, bullet_scale)

def load_crop_image(img, x, y, w, h, transform=True):
    img_original = img.subsurface((x,y),(w,h))
    if transform:
        img_scaled = pygame.transform.scale(img_original, (LARGURA_BLOCO, ALTURA_BLOCO))
        return img_scaled
    else:
        return img_original

class Base_enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, x_change):
        #renderizando sprite
        pygame.sprite.Sprite.__init__(self)
        self.speed = 10
        self.life = 2
        self.shoot_cooldown = 0
        self.x_change = x_change
        self.images_down = []
        self.images_up = []
        self.images_left = []
        self.images_right = []
        self.image_atual = []

        for c in range(0, 256, 64):
            left = load_crop_image(enemy_img, c, 96, 64, 64, False)
            left = pygame.transform.scale(left, (48,96))
            self.images_left.append(left)
            
            up = load_crop_image(enemy_img, c, 64, 64, 64, False)
            up = pygame.transform.scale(up, (48,96))
            self.images_up.append(up)
            
            if c <= 128:
                right = load_crop_image(enemy_img, c, 64, 64, 64, False)
                right = pygame.transform.scale(right, (96,128))
                self.images_right.append(right)
            
            down = load_crop_image(enemy_img, c, 0, 64, 64, False)
            down = pygame.transform.scale(down, (96,128))
            self.images_down.append(down)

        self.i = 0
        self.image_atual = self.images_down
        self.image = self.images_down[self.i]
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.pos_y_inicial = 100 - 64 - 96//2
        self.rect.topleft = (1280, 300)
    
    def update(self):
        self.i += 0.20
        if self.i >= len(self.images_down):
            self.i = 0
            self.image = self.images_down[int(self.i)]
        elif self.i >= len(self.images_right):
            self.i = 0
            self.image = self.images_right[int(self.i)]

        self.image = self.image_atual[int(self.i)]

        self.movement()

        self.colisao()

        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1
    
    # Definir movimento
    def movement(self):
        x = self.rect.x
        x_change = self.x_change

        if x <= 100:
            x_change = 5
        elif x >= 1000:
            x_change = -5

        if (x == 1000) and (len(cont) == 0):
            time.sleep(0)
            cont.append(1)
        elif (x == 1000) and (len(cont) > 0):
            time.sleep(2)
            self.image_atual = self.images_down
        elif x == 100 :
            time.sleep(2)
            self.life -= 1
            self.image_atual = self.images_right

        # colidiu = self.colisao()

        # if colidiu:
        #     if (x > 100) and (x < 1000):
        #         if x_change == 5:
        #             if x!= 550:
        #                 x_change = -5
        #         elif x_change == -5:
        #             if x!= 550:
        #                 x_change = 5


        x += x_change

        self.rect.x = x
        self.x_change = x_change

    #difinindo colisao
    # def colisao(self):
    #     collided = False

    #     if pygame.sprite.spritecollide(enemy_img, bullet_image, True):
    #         self.life -= 1
    #         collided = True
    #         time.sleep(1)

    #     return collided
            
    def enemy_shoot(self):
        if self.shoot_cooldown == 0:
            self.shoot_cooldown = shoot_cooldown
            self.bullet = Bullet(width_screen, height, self.angle)
            grupo_bullet.add(self.bullet)
            all_sprites_group.add(self.bullet)


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y , angle):
        super().__init__()
        self.image = bullet_image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.x = x
        self.y = y
        self.angle = angle
        self.speed = bullet_speed
        self.x_vel = math.cos(self.angle * (2*math.pi/360)) * self.speed
        self.y_vel = math.sin(self.angle * (2*math.pi/360)) * self.speed
        self.bullet_lifetime = bullet_lifetime
        self.spawn_time = pygame.time.get_ticks()
        self.is_shooting = False

    def bullet_movement(self):
        self.x += self.x_vel
        self.y += self.y_vel

        self.rect.x = int(self.x)
        self.rect.y = int(self.y)

        if pygame.time.get_ticks() - self.spawn_time > self.bullet_lifetime:
            self.kill()

    def update(self):
        self.bullet_movement()


# Inicializar valores
# Definir máscara de colisão