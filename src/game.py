import pygame
from time import time
from .settings import Settings
from structure.vegetation import Carvalho,Flower
        
import math
from random import randint

class World:
    def __init__(self):
        self.camera = pygame.Rect(0, 0, Settings.screen_width, Settings.screen_height)
        self.size = None


def gerate_carvalho(structure, num_arvores=500, distancia_minima=300, limite_mapa=(10000, 10000), margem=300):
    """
    Gera posições aleatórias para árvores no mapa, respeitando uma distância mínima entre elas.
    
    Parameters:
    - structure: lista onde as árvores criadas serão armazenadas.
    - num_arvores: número de árvores a serem criadas.
    - distancia_minima: distância mínima entre as árvores.
    - limite_mapa: tamanho do mapa (largura, altura).
    - margem: distância das bordas do mapa onde as árvores não serão geradas.
    """
    
    def distancia(pos1, pos2):
        """Calcula a distância euclidiana entre dois pontos."""
        return math.sqrt((pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2)

    largura_mapa, altura_mapa = limite_mapa
    
    for _ in range(num_arvores):
        while True:
            # Gera uma posição aleatória dentro do mapa, considerando as margens
            posicao = (randint(margem, largura_mapa - margem), randint(margem, altura_mapa - margem))
            
            # Verifica se a nova posição está a uma distância mínima de todas as árvores existentes
            if all(distancia(posicao, arvore.position) >= distancia_minima for arvore in structure):
                # Cria a árvore e adiciona à lista se a posição for válida
                arvore = Carvalho(position=posicao)
                structure.append(arvore)
                break  # Sai do loop ao encontrar uma posição válida

def Lsprite(imgs):
    sprites = []
    for img in imgs:
        sprites.append(pygame.image.load(img))   
        
    return sprites

cursor = 0
hora = time()

def day_cicle(screen):
    global cursor, hora
    match cursor %3:
        case 0:
            turn_time = 3 * 60
        case 1:
            turn_time = 1 * 60
        case 2:
            turn_time = 2 * 60
    
    turns = Lsprite(['assets/day.png','assets/tarde.png','assets/night.png'])
    
    if time() - hora >= turn_time:
        cursor += 1 
        hora = time()
    screen.blit(turns[cursor % 3], (0,0))



def gerate_Flower(structure, num_flores=1000, distancia_minima=100, limite_mapa=(10000, 10000), margem=300):

    def distancia(pos1, pos2):
        return math.sqrt((pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2)

    largura_mapa, altura_mapa = limite_mapa
    
    for _ in range(num_flores):
        while True:
            posicao = (randint(margem, largura_mapa - margem), randint(margem, altura_mapa - margem))
            if all(distancia(posicao,flower.position) >= distancia_minima for flower in structure):
                # Cria a árvore e adiciona à lista se a posição for válida
                flower = Flower(position=posicao)
                structure.append(flower)
                break  # Sai do loop ao encontrar uma posição válida
    
