import pygame

class Entity:
    def __init__(self, hp: int, speed: int, defesa: int, ataque: int, sprite: str, position: tuple, size: tuple):
        """ Status inicial """
        self.Hp = hp
        self.Atk = ataque
        self.Def = defesa
        self.Spd = speed
        self.Lvl = 1
        self.XP = 0
        self.alive = True

        """ Configurações iniciais """
        self.sprite = pygame.image.load(sprite)
        self.sprite = pygame.transform.scale(self.sprite, size)
        self.rect = self.sprite.get_rect(topleft=position)  

    def __str__(self):
        return f"Entidade de nível {self.Lvl} com {self.Hp} HP"

    def move(self, dx, dy):
        """ Move entidade na direção especificada """
        self.rect.x += dx * self.Spd
        self.rect.y += dy * self.Spd

    def gain_xp(self, amount):
        """ Ganha XP e sobe de nível se necessário """
        self.XP += amount
        if self.XP >= self.Lvl * 100:
            self.__level_up()
            
    def die(self):
        """ Define a entidade como morta se HP for <= 0 """
        if self.Hp <= 0:
            self.alive = False

    def __level_up(self):
        """ Sobe de nível e melhora atributos """
        self.Lvl += 1
        self.Hp += 10
        self.Atk += 4
        self.Def += 3  
        self.XP = 0

    def set_sprite(self, sprite_path):
        """ Atualiza o sprite com uma nova imagem """
        self.sprite = pygame.image.load(sprite_path)
        self.sprite = pygame.transform.scale(self.sprite, self.rect.size)

    def check_collision(self, other):
        """ Verifica colisão com outra entidade """
        return self.rect.colliderect(other.rect)

class UI:
    def __init__(self, screen):
        self.screen = screen

    def draw(self, hud):
        hud.draw(self.screen)

class HUD:
    def __init__(self, player):
        self.player = player

    def draw(self, screen):
        # Configurações de fonte
        font = pygame.font.Font(None, 36)
        
        # Exibindo informações do jogador
        hp_text = font.render(f'HP: {self.player.Hp}', True, (255, 0, 0))
        level_text = font.render(f'Nível: {self.player.Lvl}', True, (0, 255, 0))
        xp_text = font.render(f'XP: {self.player.XP}', True, (0, 0, 255))

        # Desenhar textos na tela
        screen.blit(hp_text, (10, 10))
        screen.blit(level_text, (10, 50))
        screen.blit(xp_text, (10, 90))

# Exemplo de uso no loop principal do jogo
def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()

    # Criação do jogador
    player = Entity(
        hp=100,
        speed=5,
        defesa=10,
        ataque=15,
        sprite='assets/Fump.png',
        position=(100, 100),
        size=(50, 50)
    )
    
    hud = HUD(player)
    ui = UI(screen)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Capturando teclas pressionadas para mover o jogador
        keys = pygame.key.get_pressed()
        dx, dy = 0, 0

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:   # Mover para a esquerda
            dx = -1
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:  # Mover para a direita
            dx = 1
        if keys[pygame.K_UP] or keys[pygame.K_w]:     # Mover para cima
            dy = -1
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:   # Mover para baixo
            dy = 1

        player.move(dx, dy)  # Mover o jogador
        player.gain_xp(100)
        screen.fill((0, 0, 0))  # Limpar a tela com cor preta

        # Desenhar o sprite do jogador
        screen.blit(player.sprite, player.rect)

        # Atualize o HUD na tela
        ui.draw(hud)

        pygame.display.flip()  # Atualizar a tela
        clock.tick(60)  # Limitar a 60 FPS

    pygame.quit()

if __name__ == '__main__':
    main()
