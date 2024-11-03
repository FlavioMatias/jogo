import pygame
import sys

# Configurações gerais
LARGURA, ALTURA = 1400, 800  # Dimensões da tela do jogo
FPS = 60  # Frames por segundo, controlando a taxa de atualização da tela

# Cores definidas em formato RGB
COR_PLAYER = (0, 128, 255)  # Azul claro para o jogador
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
        self.stm = 100  # Pontos de stamina

    def mover(self, teclas, camera):
        """Move o jogador de acordo com as teclas pressionadas e atualiza a posição da câmera."""
        self.velocidade = 10
        if teclas[pygame.K_LSHIFT] and self.stm > 0 :
                self.velocidade = 20
                self.stm -= 1
        else:
            if not(teclas[pygame.K_LSHIFT]):
                if self.stm < 100 :
                    self.stm += 3
                
            
            
        if teclas[pygame.K_LEFT] and self.rect.left > 5:
            self.rect.x -= self.velocidade
        if teclas[pygame.K_RIGHT] and self.rect.right < 10000:  # Limite à direita
            self.rect.x += self.velocidade
        if teclas[pygame.K_UP] and self.rect.top > 5:
            self.rect.y -= self.velocidade
        if teclas[pygame.K_DOWN] and self.rect.bottom < 10000:  # Limite embaixo
            self.rect.y += self.velocidade
        
        # Atualiza a posição da câmera baseada na posição do jogador
        camera.x = self.rect.centerx - LARGURA // 2
        camera.y = self.rect.centery - ALTURA // 2

# Classe do bloco amarelo
class BlocoAmarelo:
    def __init__(self):
        # Inicializa o retângulo do bloco amarelo em uma posição específica
        self.rect = pygame.Rect(200, 250, 40, 40)  # 40x40 pixels

# Classe do inimigo
class Inimigo:
    def __init__(self):
        # Inicializa o retângulo do inimigo e sua velocidade
        self.rect = pygame.Rect(300, 300, 40, 40)
        self.velocidade = 2  # Velocidade do inimigo

    def mover(self):
        """Move o inimigo horizontalmente e inverte a direção ao colidir com as bordas."""
        self.rect.x += self.velocidade
        if self.rect.right > 1400 or self.rect.left < 0:  # Limites de movimento
            self.velocidade = -self.velocidade

# Classe da interface do usuário
class UI:
    def __init__(self, background_image):
        self.background_image = background_image  # Imagem de fundo do jogo

    def desenhar(self, tela, player, bloco_amarelo, inimigo, camera):
        """Desenha o fundo e todos os elementos do jogo na tela, considerando a posição da câmera."""
        # Desenha o fundo
        tela.blit(self.background_image, (-camera.x, -camera.y))
        # Desenha o bloco amarelo
        pygame.draw.rect(tela, COR_BLOCO_AMARELO, (bloco_amarelo.rect.x - camera.x, bloco_amarelo.rect.y - camera.y, bloco_amarelo.rect.width, bloco_amarelo.rect.height))
        # Desenha o inimigo
        pygame.draw.rect(tela, COR_INIMIGO, (inimigo.rect.x - camera.x, inimigo.rect.y - camera.y, inimigo.rect.width, inimigo.rect.height))
        # Desenha o jogador
        tela.blit(player_sprite, (player.rect.x - camera.x, player.rect.y - camera.y))

# Classe do HUD (Heads-Up Display)
class HUD:
    def __init__(self, player):
        self.player = player  # Referência ao jogador

    def desenhar(self, tela, camera):
        """Desenha o nome do jogador e as barras de HP, MP e STM na tela."""
        font = pygame.font.SysFont(None, 36)  # Define a fonte para o texto
        # Desenha o nome do jogador acima da cabeça dele
        nome_texto = font.render(self.player.nome, True, COR_HUD)
        tela.blit(nome_texto, (self.player.rect.x + (self.player.largura // 2) - camera.x - (nome_texto.get_width() // 2), self.player.rect.y - 30 - camera.y))

        # Desenha as barras de HP, MP e STM no canto superior esquerdo
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
        self.camera = pygame.Rect(0, 0, LARGURA, ALTURA)  # Inicializa a câmera

def inicializar_jogo():
    """Inicializa o Pygame e configura a tela do jogo."""
    pygame.init()
    tela = pygame.display.set_mode((LARGURA, ALTURA))  # Cria a tela do jogo
    pygame.display.set_caption("Player na Tela")  # Define o título da janela
    return tela

def main():
    """Função principal do jogo que controla o loop do jogo e a interação com o usuário."""
    tela = inicializar_jogo()
    background_image = pygame.image.load("world.png")  # Carrega a imagem de fundo
    player = Player()  # Cria uma instância do jogador
    bloco_amarelo = BlocoAmarelo()  # Cria uma instância do bloco amarelo
    inimigo = Inimigo()  # Cria uma instância do inimigo
    ui = UI(background_image)  # Cria uma instância da interface do usuário
    hud = HUD(player)  # Cria uma instância do HUD
    world = World()  # Cria uma instância do mundo

    rodando = True  # Controle do loop principal do jogo
    while rodando:
        for evento in pygame.event.get():  # Captura eventos (como fechar a janela)
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()  # Encerra o jogo
        
        tela.fill((0,0,0))
        teclas = pygame.key.get_pressed()  # Obtém o estado das teclas pressionadas
        
        player.mover(teclas, world.camera)  # Move o jogador
        inimigo.mover()  # Move o inimigo

        ui.desenhar(tela, player, bloco_amarelo, inimigo, world.camera)  # Desenha tudo na tela
        hud.desenhar(tela, world.camera)  # Desenha o HUD

        pygame.display.flip()  # Atualiza a tela
        pygame.time.Clock().tick(FPS)  # Limita a 60 FPS

if __name__ == "__main__":
    main()  # Inicia o jogo
