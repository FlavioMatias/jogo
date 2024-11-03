import pygame
import sys
import random  # Importando a biblioteca random
import time

# Configurações gerais
LARGURA, ALTURA = 1400, 800  # Dimensões da tela do jogo
FPS = 60  # Frames por segundo, controlando a taxa de atualização da tela

# Cores definidas em formato RGB
COR_MOB = (0, 255, 128)  # Azul claro para o jogador
COR_BLOCO_AMARELO = (255, 255, 0)  # Amarelo para o bloco
COR_INIMIGO = (255, 0, 0)  # Vermelho para o inimigo
COR_HUD = (255, 255, 255)  # Cor branca para o HUD

player_sprite = pygame.image.load("assets/player.png")
player_sprite = pygame.transform.scale(player_sprite, (70, 100))

# Classe do jogador
class Player:
    def __init__(self):
        self.largura = 70  # Largura do jogador
        self.altura = 100  # Altura do jogador
        self.rect = pygame.Rect(LARGURA // 2 - self.largura // 2, ALTURA // 2 - self.altura // 2, self.largura, self.altura)
        self.velocidade = 10  # Velocidade de movimento do jogador
        self.nome = "Jogador"  # Nome do jogador
        self.hp = 100  # Pontos de vida
        self.mp = 50  # Pontos de mana
        self.stm = 75  # Pontos de stamina

    def mover(self, teclas, camera):
        """Move o jogador de acordo com as teclas pressionadas e atualiza a posição da câmera."""
        if teclas[pygame.K_LEFT] and self.rect.left > 5:
            self.rect.x -= self.velocidade
        if teclas[pygame.K_RIGHT] and self.rect.right < 10000:  # Limite à direita
            self.rect.x += self.velocidade
        if teclas[pygame.K_UP] and self.rect.top > 5:
            self.rect.y -= self.velocidade
        if teclas[pygame.K_DOWN] and self.rect.bottom < 10000:  # Limite embaixo
            self.rect.y += self.velocidade
        
        camera.x = self.rect.centerx - LARGURA // 2
        camera.y = self.rect.centery - ALTURA // 2

# Classe do bloco amarelo
class BlocoAmarelo:
    def __init__(self):
        self.rect = pygame.Rect(200, 250, 40, 40)  # 40x40 pixels
        
class Inimigo:
    def __init__(self, player):
        self.rect = pygame.Rect(300, 300, 40, 40)
        self.velocidade = 2  # Velocidade do inimigo
        self.player = player  # Referência ao jogador
        self.direcao = random.choice(['left', 'right', 'up', 'down'])
        self.tempo_troca_direcao = 1  # Tempo em segundos antes de trocar a direção
        self.ultimo_tempo = time.time()  # Tempo da última mudança de direção

    def mover(self):
        """O inimigo segue o jogador se estiver a 100 px de distância."""
        distancia_x = self.player.rect.x - self.rect.x
        distancia_y = self.player.rect.y - self.rect.y
        distancia = (distancia_x**2 + distancia_y**2)**0.5  # Distância Euclidiana

        if distancia < 200:  # Se o jogador estiver a menos de 100 px
            if abs(distancia_x) > abs(distancia_y):  # Movimentação na direção x
                if distancia_x > 0:
                    self.rect.x += self.velocidade + 5  # Move para a direita
                else:
                    self.rect.x -= self.velocidade + 5  # Move para a esquerda
            else:  # Movimentação na direção y
                if distancia_y > 0:
                    self.rect.y += self.velocidade + 5  # Move para baixo
                else:
                    self.rect.y -= self.velocidade + 5  # Move para cima
        else:
            self.movimento_aleatorio()

        # Restringir o movimento dentro dos limites da tela
        self.rect.x = max(0, min(self.rect.x, LARGURA - self.rect.width))
        self.rect.y = max(0, min(self.rect.y, ALTURA - self.rect.height))

    def movimento_aleatorio(self):
        """Movimenta o inimigo aleatoriamente."""
        if time.time() - self.ultimo_tempo > self.tempo_troca_direcao:
            self.direcao = random.choice(['left', 'right', 'up', 'down'])
            self.ultimo_tempo = time.time()  # Atualiza o tempo da última mudança

        if self.direcao == 'left':
            self.rect.x -= self.velocidade
        elif self.direcao == 'right':
            self.rect.x += self.velocidade
        elif self.direcao == 'up':
            self.rect.y -= self.velocidade
        elif self.direcao == 'down':
            self.rect.y += self.velocidade

        # Restringir o movimento dentro dos limites da tela
        self.rect.x = max(0, min(self.rect.x, LARGURA - self.rect.width))
        self.rect.y = max(0, min(self.rect.y, ALTURA - self.rect.height))


class Mob:
    def __init__(self, player):
        self.rect = pygame.Rect(500, 500, 40, 40)
        self.velocidade = 2  # Velocidade do mob
        self.player = player  # Referência ao jogador
        self.direcao = random.choice(['left', 'right', 'up', 'down'])
        self.tempo_troca_direcao = 1  # Tempo em segundos antes de trocar a direção
        self.ultimo_tempo = time.time()  # Tempo da última mudança de direção

    def mover(self):
        """O mob foge do jogador se estiver a 100 px de distância."""
        distancia_x = self.player.rect.x - self.rect.x
        distancia_y = self.player.rect.y - self.rect.y
        distancia = (distancia_x**2 + distancia_y**2)**0.5  # Distância Euclidiana

        if distancia < 300:  # Se o jogador estiver a menos de 100 px
            if abs(distancia_x) > abs(distancia_y):  # Movimentação na direção x
                if distancia_x > 0:
                    self.rect.x -= self.velocidade + 5 # Move para a esquerda
                else:
                    self.rect.x += self.velocidade + 5 # Move para a direita
            else:  # Movimentação na direção y
                if distancia_y > 0:
                    self.rect.y -= self.velocidade + 5 # Move para cima
                else:
                    self.rect.y += self.velocidade + 5 # Move para baixo
        else:
            self.movimento_aleatorio()

        # Restringir o movimento dentro dos limites da tela
        self.rect.x = max(0, min(self.rect.x, LARGURA - self.rect.width))
        self.rect.y = max(0, min(self.rect.y, ALTURA - self.rect.height))

    def movimento_aleatorio(self):
        """Movimenta o mob aleatoriamente."""
        if time.time() - self.ultimo_tempo > self.tempo_troca_direcao:
            self.direcao = random.choice(['left', 'right', 'up', 'down'])
            self.ultimo_tempo = time.time()  # Atualiza o tempo da última mudança

        if self.direcao == 'left':
            self.rect.x -= self.velocidade
        elif self.direcao == 'right':
            self.rect.x += self.velocidade
        elif self.direcao == 'up':
            self.rect.y -= self.velocidade
        elif self.direcao == 'down':
            self.rect.y += self.velocidade

        # Restringir o movimento dentro dos limites da tela
        self.rect.x = max(0, min(self.rect.x, LARGURA - self.rect.width))
        self.rect.y = max(0, min(self.rect.y, ALTURA - self.rect.height))

# Classe da interface do usuário
class UI:
    def __init__(self, background_image):
        self.background_image = background_image

    def desenhar(self, tela, player, bloco_amarelo,mob, inimigo, camera):
        tela.blit(self.background_image, (-camera.x, -camera.y))
        pygame.draw.rect(tela, COR_BLOCO_AMARELO, (bloco_amarelo.rect.x - camera.x, bloco_amarelo.rect.y - camera.y, bloco_amarelo.rect.width, bloco_amarelo.rect.height))
        pygame.draw.rect(tela, COR_INIMIGO, (inimigo.rect.x - camera.x, inimigo.rect.y - camera.y, inimigo.rect.width, inimigo.rect.height))
        pygame.draw.rect(tela, COR_MOB, (mob.rect.x - camera.x, mob.rect.y - camera.y, mob.rect.width, mob.rect.height))
        tela.blit(player_sprite, (player.rect.x - camera.x, player.rect.y - camera.y))

# Classe do HUD (Heads-Up Display)
class HUD:
    def __init__(self, player):
        self.player = player

    def desenhar(self, tela, camera):
        font = pygame.font.SysFont(None, 36)
        nome_texto = font.render(self.player.nome, True, COR_HUD)
        tela.blit(nome_texto, (self.player.rect.x + (self.player.largura // 2) - camera.x - (nome_texto.get_width() // 2), self.player.rect.y - 20 - camera.y))

        pygame.draw.rect(tela, (255, 0, 0), (10, 10, 200, 20))  # Barra de HP
        pygame.draw.rect(tela, (0, 255, 0), (10, 10, (self.player.hp / 100) * 200, 20))  # HP preenchido
        hp_texto = font.render(f"HP: {self.player.hp}", True, COR_HUD)
        tela.blit(hp_texto, (10, 10))

        pygame.draw.rect(tela, (0, 0, 255), (10, 40, 200, 20))  # Barra de MP
        pygame.draw.rect(tela, (0, 255, 255), (10, 40, (self.player.mp / 50) * 200, 20))  # MP preenchido
        mp_texto = font.render(f"MP: {self.player.mp}", True, COR_HUD)
        tela.blit(mp_texto, (10, 40))

        pygame.draw.rect(tela, (255, 255, 0), (10, 70, 200, 20))  # Barra de STM
        pygame.draw.rect(tela, (255, 0, 255), (10, 70, (self.player.stm / 75) * 200, 20))  # STM preenchido
        stm_texto = font.render(f"STM: {self.player.stm}", True, COR_HUD)
        tela.blit(stm_texto, (10, 70))

# Classe do mundo
class World:
    def __init__(self):
        self.camera = pygame.Rect(0, 0, LARGURA, ALTURA)

def inicializar_jogo():
    pygame.init()
    tela = pygame.display.set_mode((LARGURA, ALTURA))
    pygame.display.set_caption("Player na Tela")
    return tela

def main():
    tela = inicializar_jogo()
    background_image = pygame.image.load("world.png")  # Carrega a imagem de fundo
    player = Player()  # Cria uma instância do jogador
    bloco_amarelo = BlocoAmarelo()  # Cria uma instância do bloco amarelo
    inimigo = Inimigo(player)  # Cria uma instância do inimigo
    ui = UI(background_image)  # Cria uma instância da interface do usuário
    hud = HUD(player)  # Cria uma instância do HUD
    world = World()  # Cria uma instância do mundo
    mob = Mob(player)
    rodando = True
    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        tela.fill((0, 0, 0))
        teclas = pygame.key.get_pressed()
        player.mover(teclas, world.camera)  # Move o jogador
        mob.mover()
        inimigo.mover()  # Move o inimigo

        ui.desenhar(tela, player, bloco_amarelo, mob, inimigo, world.camera)
        hud.desenhar(tela, world.camera)

        pygame.display.flip()
        pygame.time.Clock().tick(FPS)

if __name__ == "__main__":
    main()  # Inicia o jogo
