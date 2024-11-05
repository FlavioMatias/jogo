from ._base import Structure
import pygame
from time import time

class Carvalho(Structure):
    def __init__(self, position, sprite = "assets/Tree.png", size = (200,240)):
        super().__init__(sprite, size, position, rect_height= 2)
        self.fase_cursor = 0
        self.Sprites_fase = self.Lsprite(['assets/Tree3.png','assets/Tree2.png','assets/Tree1.png'])
        self.sprite = self.Sprites_fase[self.fase_cursor]
        
        self.rise = time()
        self.new_fase = 5
        
    
    def grow(self):
        if (time() - self.rise > self.new_fase) and self.fase_cursor < 2:
            self.fase_cursor += 1
            self.sprite = self.Sprites_fase[self.fase_cursor]
            self.rise = time()
        
        
        
    def Lsprite(self, imgs):
        sprites = []
        for index, img in enumerate(imgs):
            img_sprite = pygame.image.load(img)
            new_size = (66 * (index + 1), 80 * (index + 1)) 
            img_sprite = pygame.transform.scale(img_sprite, new_size)
            sprites.append(img_sprite)
        
        return sprites