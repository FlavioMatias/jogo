import pygame

class Structure:
    def __init__(self, sprite: str, size: tuple, position: tuple, rect_height: int = 1, collision_offset: tuple = (0, 0)):
        self.sprite = pygame.image.load(sprite)
        self.sprite = pygame.transform.scale(self.sprite, size)

        self.rect = self.sprite.get_rect()  # Retângulo do sprite
        self.rect.topleft = position
        
        # Definir o retângulo de colisão, com offset se necessário
        self.collision_rect = pygame.Rect(position[0] + collision_offset[0], position[1] + collision_offset[1], size[0], rect_height)

        self.position = position
        self.size = size
        self.rect_height = rect_height

    def check_collision(self, entities):
        """Verifica e resolve colisão com entidades, permitindo passagem na metade superior"""
        for entity in entities:
            if entity != self and self.collision_rect.colliderect(entity.collision_rect):
                if entity.last_direction == "up" or entity.last_direction == "down":
                    # 3. Colisão embaixo (evita que a entidade ultrapasse a parte inferior)
                    if self.collision_rect.bottom > entity.collision_rect.top and self.collision_rect.top < entity.collision_rect.top:
                        entity.rect.y += entity.Spd 

                    # 4. Colisão em cima (evita que a entidade ultrapasse a parte superior)
                    elif self.collision_rect.top < entity.collision_rect.bottom and self.collision_rect.bottom > entity.collision_rect.bottom:
                        entity.rect.y -= entity.Spd               

                if entity.last_direction == "right" or entity.last_direction == "left":
                    # 1. Colisão na direita
                    if self.collision_rect.right > entity.collision_rect.left and self.collision_rect.left < entity.collision_rect.left:
                        entity.rect.x += entity.Spd  

                    # 2. Colisão na esquerda
                    elif self.collision_rect.left < entity.collision_rect.right and self.collision_rect.right > entity.collision_rect.right:
                        entity.rect.x -= entity.Spd   
