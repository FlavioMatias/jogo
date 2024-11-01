from ._base import Entity, Inventory
import pygame

class Player(Entity):
        def __init__(self, hp: int, speed: int, defesa: int, ataque: int, sprite: str, position: tuple, size: tuple, name: str):

            super().__init__(hp, speed, defesa, ataque, sprite, position, size)
            self.nick = name  
            self.inventory = Inventory()
            self.saciedade = 100
            self.atriubutos = Attributes()
            
        def move(self, keys):
            delta_x = 0
            delta_y = 0

            if keys[pygame.K_a]: 
                delta_x = -self.Spd
            if keys[pygame.K_d]: 
                delta_x = self.Spd
            if keys[pygame.K_w]: 
                delta_y = -self.Spd
            if keys[pygame.K_s]: 
                delta_y = self.Spd

            self.rect.x += delta_x
            self.rect.y += delta_y

            
            self.rect.x = max(0, min(self.rect.x, 1450))
            self.rect.y = max(0, min(self.rect.y, 830))
        def gain_xp(self, amount):
            """ Ganha XP e sobe de nível se necessário """
            
            self.XP += amount
            if self.XP >= self.Lvl * 100:
                self.__level_up()
            
        def __level_up(self):
            """ Sobe de nível e melhora atributos """
            
            self.Lvl += 1
            self.Hp += 20
            self.Atk += 10
            self.Def += 5 
            self.XP = max(0, self.XP - (self.Lvl - 1) * 100) 
            
        def atack(self):
            pass
        
        
class Atributes:
    def _