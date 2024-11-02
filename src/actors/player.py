from ._base import Entity, Inventory
import pygame
class raça:
    pass
    # raças = [anao, elfo, hobbit, humano]
class Player(Entity):
        def __init__(self, sprite : str, position: tuple, size: tuple, name: str, speed: int = 10, max_hp: int = 100):

            super().__init__(max_hp, speed, sprite, position, size)
            self.nick = name  
            self._Max_MP = 100
            self.MP = self._Max_MP
            self._Max_STM = 100
            self.STM = self._Max_STM
            self.moedas = 0
            self.equipamentos = Equipamentos()
            self.inventory = Inventory()
            self.atriubutos = Attributes()
            
        def move(self, keys):
            delta_x = 0
            delta_y = 0

            if keys[pygame.K_a]: 
                delta_x = -self.Spd
                self.STM -= 0.1
            if keys[pygame.K_d]: 
                delta_x = self.Spd
                self.STM -= 0.1
            if keys[pygame.K_w]: 
                delta_y = -self.Spd
                self.STM -= 0.1
            if keys[pygame.K_s]: 
                delta_y = self.Spd
                self.STM -= 0.1

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
            self.MaxHP += 20
            self.XP = max(0, self.XP - (self.Lvl - 1) * 100) 
            
        def atack(self):
            pass
        
        
class Attributes:
    def __init__(self):
        self.intelligence: int = 0
        self.strength: int = 0
        self.agility: int = 0
        self.dexterity: int = 0
        self.constitution: int = 0
        self.wisdom: int = 0
        self.charisma: int = 0

class Equipamentos():
    def __init__(self):
        pass