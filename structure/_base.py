import pygame

class Structure:
    def __init__(self, sprite: str, size: tuple, position: tuple, rect_height: int = 1):
        # Carrega o sprite e redimensiona para o tamanho desejado
        self.sprite = pygame.image.load(sprite)
        self.sprite = pygame.transform.scale(self.sprite, size)

        # Define `self.rect` baseado no `sprite` redimensionado
        self.rect = self.sprite.get_rect()  
        self.rect.topleft = position  # Define a posição inicial
        
        # Guarda as propriedades iniciais
        self.position = position
        self.size = size
        self.rect_height = rect_height

    def check_collision(self, entities):
        """ Verifica e resolve colisão com entidades, permitindo passagem na metade superior """
        colisores = entities

        # Define a "área de colisão" apenas na metade inferior de `self`
        collision_rect = self.collision_rect  # Use o collision_rect pequeno
        for entity in colisores:
            if entity != self and collision_rect.colliderect(entity.rect):  # Verifica colisão
                dx_right = entity.rect.left - self.rect.right
                dx_left = entity.rect.right - self.rect.left
                dy_bottom = entity.rect.top * 20 - self.rect.bottom
                dy_top = entity.rect.bottom - self.rect.top

                # Ajusta a distância de colisão para permitir uma resolução mais precisa
                if abs(dx_right) < abs(dy_bottom) and abs(dx_right) < abs(dy_top):
                    entity.rect.left = self.rect.right  # Empurra para a direita
                elif abs(dx_left) < abs(dy_bottom) and abs(dx_left) < abs(dy_top):
                    entity.rect.right = self.rect.left  # Empurra para a esquerda
                elif abs(dy_bottom) < abs(dx_right) and abs(dy_bottom - 20) < abs(dx_left):
                    entity.rect.top = self.rect.bottom  # Empurra para cima
                elif abs(dy_top) < abs(dx_right) and abs(dy_top) < abs(dx_left):
                    entity.rect.bottom = self.rect.top  # Empurra para baixo

        return any(collision_rect.colliderect(entity.rect) for entity in colisores if entity != self)

