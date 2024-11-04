import pygame

class Projectile:
    def __init__(self, position : tuple, sprite : str, size : tuple):
        self.sprite = pygame.image.load(sprite)
        self.sprite = pygame.transform.scale(self.sprite, size)
        self.rect = self.sprite.get_rect(topleft=position)  
        self.
        
        
    def colision(self, entities):
        
    def die(self):
        """ Define a entidade como morta se HP for <= 0 """
        
        if self.Hp <= 0:
            self.alive = False

        
    def move():
        
class Hand(Projectile):
    def __init__(self, position, sprite ="assets/Fump.png" , size = (20,20)):
        super().__init__(position, sprite, size)