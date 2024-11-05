import pygame

class Structure:
    def __init__(self,sprite : str, size : tuple, position : tuple, rect_height : int = 1):
        self.sprite = pygame.image.load(sprite)
        self.sprite = pygame.transform.scale(self.sprite, size)
        self.rect = self.rect = pygame.Rect(position, size)
        self.position = position
        self.size = size
        self.rect_height = rect_height
    def check_collision(self, entities):
        """ Verifica e resolve colisão com entidades, permitindo passagem na metade superior """
        
        colisores = entities  # Lista com as entidades a serem verificadas
        
        # Define a "área de colisão" apenas na metade inferior de `self`
        collision_rect = self.rect.copy()
        collision_rect.height //= self.rect_height  

        # Move `collision_rect` para a parte inferior do retângulo original
        collision_rect.top += (self.rect_height - 1) * collision_rect.height
        # Verifica a colisão com cada entidade na metade inferior
        for entity in colisores:
            if entity != self and collision_rect.colliderect(entity.rect):  # Verifica colisão na parte inferior
                # Calcula as distâncias horizontais e verticais entre os retângulos
                dx_right = entity.rect.left - self.rect.right
                dx_left = entity.rect.right - self.rect.left
                dy_bottom = entity.rect.top - self.rect.bottom
                dy_top = entity.rect.bottom - self.rect.top

                # Verifica qual é a menor distância de colisão (horizontal ou vertical)
                if abs(dx_right) < abs(dy_bottom) and abs(dx_right) < abs(dy_top):
                    # Colisão pelo lado direito
                    entity.rect.left = self.rect.right
                elif abs(dx_left) < abs(dy_bottom) and abs(dx_left) < abs(dy_top):
                    # Colisão pelo lado esquerdo
                    entity.rect.right = self.rect.left
                elif abs(dy_bottom) < abs(dx_right) and abs(dy_bottom - 20) < abs(dx_left):
                    # Colisão por baixo
                    entity.rect.top = self.rect.bottom
                elif abs(dy_top) < abs(dx_right) and abs(dy_top) < abs(dx_left):
                    # Colisão por cima
                    entity.rect.bottom = self.rect.top

        # Retorna True se houver colisão na metade inferior, ou False se não houver
        return any(collision_rect.colliderect(entity.rect) for entity in colisores if entity != self)