import pygame
from pygame.locals import *
import time

pygame.init()
# Criar classe de inimigo
enemy_img = pygame.image.load('Projeto/assets/coruja-Sheet.png')

def load_crop_image(img, x, y, w, h, transform=True):
    img_original = img.subsurface((x,y),(w,h))
    if transform:
        img_scaled = pygame.transform.scale(img_original, (LARGURA_BLOCO, ALTURA_BLOCO))
        return img_scaled
    else:
        return img_original

class base_enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, x_change):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 10
        self.life = 2
        self.x_change = x_change
        self.images_down = []
        self.images_up = []
        self.images_left = []
        self.images_right = []
        self.image_atual = []

        for c in range(0, 448, 64):
            left = load_crop_image(enemy_img, c, 96, 64, 64, False)
            left = pygame.transform.scale(left, (48,96))
            self.images_left.append(left)
            
            up = load_crop_image(enemy_img, c, 64, 64, 64, False)
            up = pygame.transform.scale(up, (48,96))
            self.images_up.append(up)
            
            right = load_crop_image(enemy_img, c, 32, 64, 64, False)
            right = pygame.transform.scale(right, (48,96))
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
        self.rect.topleft = (500, 300)
    
    def update(self):
        self.i += 0.20
        if self.i >= len(self.images_down):
            self.i = 0
        self.image = self.image_atual[int(self.i)]
    
    # Definir movimento
    def movement(self):
        x = self.x
        x_change = self.x_change

        if x <= 100:
            x_change = 5
        elif x >= 900:
            x_change = -5

        if (x == 900) and (len(cont) == 0):
            time.sleep(0)
            cont.append(1)
        elif (x == 900) and (len(cont) > 0):
            time.sleep(1.5)
        elif x == 100 :
            time.sleep(1.5)
        elif self.colisao():
            time.sleep(1)

        x += x_change

        self.colisao()

        self.x = x
        self.x_change = x_change

    def colisao(self):
        collided = False

        if self.x == 100:
            collided = True

        if collided:
            self.life -= 1

        return collided

# Inicializar valores
width_screen = 1280
width = 1050
height = 200
pause = [1,2,3,4,5,6,7,8,9,10,11,12,13]
cont = []
# Renderizar sprite
# Definir máscara de colisão