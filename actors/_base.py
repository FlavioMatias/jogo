import pygame

class Entity:
    def __init__(self, max_hp : int, speed: int, sprite: str, position: tuple, size: tuple):
        """ Status inicial """
        self.HP = max_hp
        self._Max_Hp = max_hp
        self.Spd = speed
        self._Lvl = 1
        self.XP = 0
        self.alive = True
        self.size = size



        """ configuraçoes iniciais """
        self.sprite = pygame.image.load(sprite)
        self.sprite = pygame.transform.scale(self.sprite, size)
        self.rect = self.sprite.get_rect(topleft=position)  
        self.collision_rect = pygame.Rect(
            self.rect.centerx - 15,  # posição X centralizada
            self.rect.bottom - (self.rect.height // 2),  # Começa da metade inferior da entidade
            35, 35                   # Tamanho da área de colisão
        )
        
    def __str__(self):
        return f"Entidade de nível {self.Lvl} com {self.Hp} HP"

    def move(self, dx, dy):
        """ Move entidade na direção especificada """
        
        self.rect.x += dx * self.Spd
        self.rect.y += dy * self.Spd

    def gain_xp(self, amount):
        """ Ganha XP e sobe de nível se necessário """
        
        self.XP += amount
        if self.XP >= self.Lvl * 120:
            self.__level_up()
            
    def die(self):
        """ Define a entidade como morta se HP for <= 0 """
        
        if self.Hp <= 0:
            self.alive = False

    def __level_up(self):
        """ Sobe de nível e melhora atributos """
        
        self.Lvl += 1
        self.Hp += 10  
        self.XP = max(0, self.XP - (self.Lvl - 1) * 120)

    def set_sprite(self, sprite_path):
        """ Atualiza o sprite com uma nova imagem """
        
        self.sprite = pygame.image.load(sprite_path)
        self.sprite = pygame.transform.scale(self.sprite, self.rect.size)

    def check_collision(self, other):
        """ Verifica colisão com outra entidade """

        return self.rect.colliderect(other.rect)

class Inventory:
    def __init__(self):
        self.items = {}
        
    def add_item(self, item: object, quantity: int):
        if item.name in self.items:
            self.items[item.name]['quantity'] += quantity  
        else:
            self.items[item.name] = {'quantity': quantity, 'item': item}  # Adiciona o item aqui

        
    def use_item(self, item_name : str, user : int):
        if item_name in self.items and self.items[item_name]['quantity'] > 0:
            item = self.items[item_name]['item']
            if item.consume(user):
                self.items[item_name]['quantity'] -= 1  
                if self.items[item_name]['quantity'] == 0:
                    del self.items[item_name]  
                return True  
        return False 
    
    def drop_item(self, item_name: str, quantity: int):
        if item_name in self.items:
            if self.items[item_name]['quantity'] > quantity:
                self.items[item_name]['quantity'] -= quantity
                return {item_name: quantity}
            elif self.items[item_name]['quantity'] == quantity:
                dropped_item = {item_name: self.items[item_name]['quantity']}
                del self.items[item_name]
                return dropped_item
        return None

            
    
class Skill:
    pass
