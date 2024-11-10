from ._base import Structure
import pygame
from time import time
from random import randint, choice

import pygame
from time import time

class Carvalho(Structure):
    def __init__(self, position, sprite="assets/Tree.png", size=(200, 240)):
        super().__init__(sprite, size, position, rect_height=2)
        
        self.fase_cursor = randint(0, 2)
        self.Sprites_fase = self.Lsprite(['assets/Tree3.png', 'assets/Tree2.png', 'assets/Tree1.png'])
        
        self.sprite = self.Sprites_fase[self.fase_cursor]
        self.rect = self.sprite.get_rect(midbottom=position)
        
        # Cria um retângulo de colisão menor, agora com tamanho fixo de 10x10 pixels
        self.collision_rect = pygame.Rect(
            self.rect.centerx - 20,  # posição x, centralizando o quadrado pequeno
            self.rect.bottom - 40,  # posição y, mantendo próximo ao fundo da árvore
            50, 35                  # largura e altura do retângulo de colisão
        )

        self.rise = time()
        self.new_fase = 5 * 60

    def grow(self):
        if (time() - self.rise > self.new_fase) and self.fase_cursor < len(self.Sprites_fase) - 1:
            self.fase_cursor += 1
            self.sprite = self.Sprites_fase[self.fase_cursor]
            self.rect = self.sprite.get_rect(midbottom=self.rect.midbottom)

            # Atualiza a posição do collision_rect para acompanhar o crescimento
            self.collision_rect.midbottom = self.rect.midbottom


            self.rise = time()

    def Lsprite(self, imgs):
        sprites = []
        for index, img in enumerate(imgs):
            img_sprite = pygame.image.load(img).convert_alpha()
            new_size = (66 * (index + 1), 80 * (index + 1))
            img_sprite = pygame.transform.scale(img_sprite, new_size)
            sprites.append(img_sprite)
        
        return sprites
    

class Flower:
    def __init__(self, position : tuple):
        self.img = choice(["flor1.png","flor3.png","flor2.png"])
        self.sprite = pygame.image.load(self.img)
        self.sprite = pygame.transform.scale(self.sprite, (35,40))
        self.rect = self.sprite.get_rect()
        self.position = position
        self.rect.topleft = position

    def check_collision(self, entity):pass


class Lago(Structure):
    def __init__(self, position, sprite="Frame 14.png", size=(600, 500)):
        super().__init__(sprite, size, position, rect_height=2)
        self.rect = self.sprite.get_rect(midbottom=position)
        
        # Cria um retângulo de colisão menor, agora com tamanho fixo de 10x10 pixels
        self.collision_rect = pygame.Rect(
            self.rect.centerx,  # posição x, centralizando o quadrado pequeno
            self.rect.bottom,  # posição y, mantendo próximo ao fundo da árvore
            size                  # largura e altura do retângulo de colisão
        )
    def check_collision(self, entities):pass
