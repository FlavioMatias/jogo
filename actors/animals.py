import random
import time
import pygame
from src.settings import Settings

LARGURA, ALTURA = Settings.world_size

class Mob:
    def __init__(self, player):
        self.sprite = pygame.image.load("assets/coelho_1.png")
        self.sprite = pygame.transform.scale(self.sprite, (50,50))
        self.rect = self.sprite.get_rect(topleft=(500, 500))  
        self.Spd = 4  # Velocidade do mob
        self.alive = True
        self.player = player  # Referência ao jogador
        self.direcao = random.choice(['left', 'right', 'up', 'down', 'stop'])
        self.tempo_troca_direcao = random.randint(1, 3)  # Tempo em segundos antes de trocar a direção
        self.ultimo_tempo = time.time()  # Tempo da última mudança de direção

    def move(self):
        """O mob foge do jogador se estiver a 100 px de distância."""
        distancia_x = self.player.rect.x - self.rect.x
        distancia_y = self.player.rect.y - self.rect.y
        distancia = (distancia_x**2 + distancia_y**2)**0.5  # Distância Euclidiana

        if distancia < 200:  # Se o jogador estiver a menos de 100 px
            if abs(distancia_x) > abs(distancia_y):  # Movimentação na direção x
                if distancia_x > 0:
                    self.rect.x -= self.Spd + 10 # Move para a esquerda
                else:
                    self.rect.x += self.Spd + 10 # Move para a direita
            else:  # Movimentação na direção y
                if distancia_y > 0:
                    self.rect.y -= self.Spd + 10 # Move para cima
                else:
                    self.rect.y += self.Spd + 10 # Move para baixo
        else:
            self.movimento_aleatorio()

        # Restringir o movimento dentro dos limites da tela
        self.rect.x = max(0, min(self.rect.x, LARGURA - self.rect.width))
        self.rect.y = max(0, min(self.rect.y, ALTURA - self.rect.height))

    def movimento_aleatorio(self):
        """Movimenta o mob aleatoriamente."""
        if time.time() - self.ultimo_tempo > self.tempo_troca_direcao:
            self.direcao = random.choice(['left', 'right', 'up', 'down', 'stop'])
            self.ultimo_tempo = time.time()
            self.tempo_troca_direcao = random.randint(1,3)# Atualiza o tempo da última mudança

        if self.direcao == 'left':
            self.rect.x -= self.Spd
        elif self.direcao == 'right':
            self.rect.x += self.Spd
        elif self.direcao == 'up':
            self.rect.y -= self.Spd
        elif self.direcao == 'down':
            self.rect.y += self.Spd
        if self.direcao == 'stop':
            pass

        # Restringir o movimento dentro dos limites da tela
        self.rect.x = max(0, min(self.rect.x, LARGURA - self.rect.width))
        self.rect.y = max(0, min(self.rect.y, ALTURA - self.rect.height))
