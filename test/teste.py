import pygame
import random
import math

# Inicializando Pygame
pygame.init()

# Configurações da tela
WIDTH, HEIGHT = 800, 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Quadrados com IA")

# Configurações dos quadrados
SQUARE_SIZE = 20
GREEN, BLUE, RED, WHITE = (0, 255, 0), (0, 0, 255), (255, 0, 0), (255, 255, 255)
SPEED = 2
ESCAPE_SPEED = SPEED + 2  # Velocidade de fuga do quadrado vermelho

# Posições iniciais dos quadrados
green_square = pygame.Rect(random.randint(0, WIDTH), random.randint(0, HEIGHT), SQUARE_SIZE, SQUARE_SIZE)
blue_square = pygame.Rect(random.randint(0, WIDTH), random.randint(0, HEIGHT), SQUARE_SIZE, SQUARE_SIZE)
red_square = pygame.Rect(random.randint(0, WIDTH), random.randint(0, HEIGHT), SQUARE_SIZE, SQUARE_SIZE)

# Função de movimento com IA para perseguir o quadrado vermelho
def move_towards(target, follower, speed=SPEED):
    dx, dy = target.x - follower.x, target.y - follower.y
    dist = math.hypot(dx, dy)
    if dist > 0:
        follower.x += int(dx / dist * speed)
        follower.y += int(dy / dist * speed)

# Função de movimento para fuga com antecipação de movimento
def move_away(follower, chasers, escape_speed=ESCAPE_SPEED):
    total_dx, total_dy = 0, 0
    for chaser in chasers:
        # Distância e direção do perseguidor para o quadrado vermelho
        dx, dy = chaser.x - follower.x, chaser.y - follower.y
        dist = math.hypot(dx, dy)
        if dist > 0 and dist < 150:  # Aumenta o range de detecção
            # Calcula a direção oposta ao perseguidor e acumula
            total_dx -= dx / dist
            total_dy -= dy / dist
            
            # Antecipação de movimento: evita o perseguidor de forma mais complexa
            # Se o perseguidor está se movendo para o quadrado vermelho, adiciona um desvio
            total_dx -= (dx / dist) * 0.5
            total_dy -= (dy / dist) * 0.5

    # Normaliza o vetor de fuga e ajusta a velocidade
    dist = math.hypot(total_dx, total_dy)
    if dist > 0:
        follower.x += int(total_dx / dist * escape_speed)
        follower.y += int(total_dy / dist * escape_speed)

# Loop principal
clock = pygame.time.Clock()
running = True

while running:
    window.fill(WHITE)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Movimentação dos quadrados com IA
    move_towards(red_square, green_square)
    move_towards(red_square, blue_square)
    move_away(red_square, [green_square, blue_square])

    # Mantém os quadrados dentro da tela
    for square in [green_square, blue_square, red_square]:
        if square.x < 0: square.x = 0
        elif square.x > WIDTH - SQUARE_SIZE: square.x = WIDTH - SQUARE_SIZE
        if square.y < 0: square.y = 0
        elif square.y > HEIGHT - SQUARE_SIZE: square.y = HEIGHT - SQUARE_SIZE

    # Desenha os quadrados
    pygame.draw.rect(window, GREEN, green_square)
    pygame.draw.rect(window, BLUE, blue_square)
    pygame.draw.rect(window, RED, red_square)
    
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
