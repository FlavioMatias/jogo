import pygame
import sys

# Configurações gerais
LARGURA, ALTURA = 800, 600  # Dimensões da tela do jogo
FPS = 60  # Frames por segundo, controlando a taxa de atualização da tela

# Cores definidas em formato RGB
COR_PLAYER = (0, 128, 255)  # Azul claro para o jogador
COR_BLOCO_AMARELO = (255, 255, 0)  # Amarelo para o bloco
COR_INIMIGO = (255, 0, 0)  # Vermelho para o inimigo

# Classe do jogador
class Player:
    def __init__(self):
        self.largura = 50  # Largura do jogador
        self.altura = 50  # Altura do jogador
        # Inicializa o retângulo do jogador centralizado na tela
        self.rect = pygame.Rect(LARGURA // 2 - self.largura // 2, ALTURA // 2 - self.altura // 2, self.largura, self.altura)
        self.velocidade = 10  # Velocidade de movimento do jogador

    def mover(self, teclas, camera):
        """Move o jogador de acordo com as teclas pressionadas e atualiza a posição da câmera."""
        # Movimentos com as teclas de seta
        if teclas[pygame.K_LEFT] and self.rect.left > 5:
            self.rect.x -= self.velocidade
        if teclas[pygame.K_RIGHT] and self.rect.right < 1440:  # Limite à direita
            self.rect.x += self.velocidade
        if teclas[pygame.K_UP] and self.rect.top > 5:
            self.rect.y -= self.velocidade
        if teclas[pygame.K_DOWN] and self.rect.bottom < 820:  # Limite embaixo
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
        pygame.draw.rect(tela, COR_PLAYER, (player.rect.x - camera.x, player.rect.y - camera.y, player.largura, player.altura))

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
    background_image = pygame.image.load("background_glass.png")  # Carrega a imagem de fundo
    player = Player()  # Cria uma instância do jogador
    bloco_amarelo = BlocoAmarelo()  # Cria uma instância do bloco amarelo
    inimigo = Inimigo()  # Cria uma instância do inimigo
    ui = UI(background_image)  # Cria uma instância da interface do usuário
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

        pygame.display.flip()  # Atualiza a tela
        pygame.time.Clock().tick(FPS)  # Limita a 60 FPS

if __name__ == "__main__":
    main()  # Executa a função principal ao rodar o script


"""Explicação Detalhada de Cada Parte
Imports:

import pygame: Importa a biblioteca Pygame, que é usada para criar jogos em Python.
import sys: Importa o módulo sys, que é usado para encerrar o programa.
Configurações Gerais:

LARGURA e ALTURA: Define as dimensões da tela do jogo.
FPS: Controla quantos frames por segundo o jogo deve atualizar, afetando a suavidade do movimento.
Cores:

Definidas como tuplas RGB (Red, Green, Blue), facilitando a mudança de cores no jogo.
Classe Player:

Responsável por representar o jogador no jogo.
Contém atributos como largura, altura, e velocidade, além de um retângulo (rect) que representa a posição e as dimensões do jogador.
O método mover() atualiza a posição do jogador com base nas teclas pressionadas e ajusta a posição da câmera.
Classe BlocoAmarelo:

Representa um bloco amarelo no jogo.
Contém um retângulo que define a sua posição e tamanho.
Classe Inimigo:

Representa um inimigo que se move automaticamente.
O método mover() faz o inimigo se mover de um lado para o outro na tela e inverte sua direção ao colidir com os limites.
Classe UI (Interface do Usuário):

Controla a renderização dos elementos do jogo na tela.
O método desenhar() é responsável por desenhar a imagem de fundo e todos os elementos (jogador, bloco, inimigo) na tela, ajustando suas posições de acordo com a câmera.
Classe World:

Representa o mundo do jogo, contendo a câmera que controla a visão do jogador.
Função inicializar_jogo():

Inicializa o Pygame, configura a tela e define o título da janela do jogo.
Função main():

Controla o loop principal do jogo, onde eventos são capturados, o estado do jogo é atualizado e a tela é desenhada.
Instâncias das classes são criadas e métodos são chamados para mover o jogador e o inimigo e desenhar a interface do usuário.
Estrutura do Loop Principal:

O loop continua enquanto a variável rodando for verdadeira. Ele captura eventos (como a solicitação de fechar a janela), processa entradas do usuário (teclado), atualiza as posições dos objetos e desenha tudo na tela.
Seção de Execução:

if __name__ == "__main__": garante que a função main() seja chamada quando o script é executado diretamente, iniciando o jogo.
Resumo
Este código é uma base simples para um jogo 2D em Python utilizando a biblioteca Pygame. Ele inclui um jogador que pode ser movido com as teclas de seta, um bloco amarelo estático e um inimigo que se move automaticamente. A interface do usuário é gerenciada para garantir que todos os elementos sejam desenhados corretamente na tela, considerando a posição da câmera.

Se você tiver mais perguntas ou precisar de mais detalhes sobre alguma parte específica, é só avisar!"""