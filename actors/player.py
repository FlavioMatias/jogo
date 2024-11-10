from ._base import Entity, Inventory
from src.settings import Settings
import pygame
from time import time

class Raça:
    def __init__(self):

        self.sprite_up = self.Lsprite(['assets/_Player/back_Stop.png', 'assets/_Player/backF1.png','assets/_Player/back_Stop.png', 'assets/_Player/backF2.png'])
        self.sprite_down = self.Lsprite(['assets/_Player/Front_stop.png', 'assets/_Player/FrontF1.png','assets/_Player/Front_stop.png', 'assets/_Player/FrontF2.png'])
        self.sprite_left = self.Lsprite(['assets/_Player/left_stop.png', 'assets/_Player/leftF1.png','assets/_Player/left_stop.png', 'assets/_Player/leftF2.png'])
        self.sprite_right = self.Lsprite(['assets/_Player/right_stop.png', 'assets/_Player/rightF1.png','assets/_Player/right_stop.png', 'assets/_Player/rightF2.png'])
    
    def Lsprite(self, imgs):
        sprites = []
        for img in imgs:
            sprites.append(pygame.image.load(img))   
            
        return sprites

        

    # raças = [anao, elfo, hobbit, humano]
class Player(Entity):
        def __init__(self, sprite : str, position: tuple, name: str, size: tuple = (50, 55), speed: int = 10, max_hp: int = 100):

            super().__init__(max_hp, speed, sprite, position, size)
            self.nick = name  
            self._Max_MP = 100
            self.MP = self._Max_MP
            self._Max_STM = 100
            self.STM = self._Max_STM
            self.atk_spd = 1
            
            self.moedas = 0
            self.equipamentos = Equipamentos()
            self.inventory = Inventory()
            self.atriubutos = Attributes()
            self.race = Raça()
            
            self.last_hit = time()
            
            self.frame = 0
            self.last_frame = time()
            self.animation_spd = 0.2
            self.last_direction = "down"    

            self.collision_rect = pygame.Rect(
                self.rect.centerx - 15, 
                self.rect.bottom - (self.rect.height // 2) - 10,  
                40, 35                   # Tamanho da área de colisão
            )            
                
        def move(self, teclas, camera):
            """Move o jogador de acordo com as teclas pressionadas e atualiza a posição da câmera."""
            self.__spliter(teclas)
            move = False
            
            # Movendo para a esquerda (verifica se `lefth` é True)
            if teclas[pygame.K_a] :
                self.rect.x -= self.Spd
                self.last_direction = "left"
                self.sprite = self.race.sprite_left[self.frame % 4]
                move = True

            # Movendo para a direita (verifica se `righth` é True)
            if teclas[pygame.K_d]:
                self.rect.x += self.Spd
                self.last_direction = "right"
                self.sprite = self.race.sprite_right[self.frame % 4]
                move = True

            # Movendo para cima (verifica se `uph` é True)
            if teclas[pygame.K_w]:
                self.rect.y -= self.Spd
                self.last_direction = "up"
                self.sprite = self.race.sprite_up[self.frame % 4]
                move = True

            # Movendo para baixo (verifica se `downh` é True)
            if teclas[pygame.K_s] :
                self.rect.y += self.Spd
                self.last_direction = "down"
                self.sprite = self.race.sprite_down[self.frame % 4]
                move = True

            if teclas[pygame.K_s] and teclas[pygame.K_w] and not(teclas[pygame.K_d] or  teclas[pygame.K_a]) or teclas[pygame.K_d] and  teclas[pygame.K_a] and not(teclas[pygame.K_s] or teclas[pygame.K_w]):
                self.sprite = self.race.sprite_down[0]
                
            if move:
                if time() - self.last_frame > self.animation_spd:
                    self.last_frame = time()
                    self.frame += 1

            if not move:
                self.frame = 0
                match self.last_direction:
                    case 'down':
                        self.sprite = self.race.sprite_down[0]
                    case 'up':
                        self.sprite = self.race.sprite_up[0]
                    case 'left':
                        self.sprite = self.race.sprite_left[0]
                    case 'right':
                        self.sprite = self.race.sprite_right[0]

            self.sprite = pygame.transform.scale(self.sprite, self.size)
            self.collision_rect.x = self.rect.centerx - 20  # Ajusta a posição X do collision_rect
            self.collision_rect.y = self.rect.bottom - (self.rect.height // 2) + 15  

            
            if Settings.fullscreen:
                
                camera.x = self.rect.centerx - 1920 // 2
                camera.y = self.rect.centery - 1080 // 2

                # Ajusta as coordenadas para não ultrapassar os limites do mapa
                self.rect.x = max(0, min(self.rect.x, 10000 - self.size[0]))  # Subtrai o tamanho do jogador para evitar que ele ultrapasse
                self.rect.y = max(0, min(self.rect.y, 10000 - self.size[1]))  # O mesmo para a coordenada y
                
            else:
                camera.x = self.rect.centerx - Settings.screen_width // 2
                camera.y = self.rect.centery - Settings.screen_height // 2

                # Ajusta as coordenadas para não ultrapassar os limites do mapa
                self.rect.x = max(0, min(self.rect.x, 10000 - self.size[0]))  # Subtrai o tamanho do jogador para evitar que ele ultrapasse
                self.rect.y = max(0, min(self.rect.y, 10000 - self.size[1]))  # O mesmo para a coordenada y

        def __spliter(self, key):
            if key[pygame.K_LSHIFT] and self.STM > 1 and (key[pygame.K_s] or key[pygame.K_w] or key[pygame.K_a] or key[pygame.K_d]):
                self.Spd = 17
                self.animation_spd = 0.1
                self.STM -= 1
            else:
                self.Spd = 10
                self.animation_spd = 0.2
                
            
            
            
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
            
        def atack(self, Key):
            if time() - self.last_hit > self.atk_spd:
                if Key[0] and self.STM > 10:
                    self.STM -= 10
                    self.last_hit = time()
                
        def player_recover(self, keymouse, key):
            
            if self.HP < self._Max_Hp:
                self.HP += 0.1
            if self.STM < self._Max_STM and not keymouse[0] and not key[pygame.K_LSHIFT]:
                self.STM += 1
            
        
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