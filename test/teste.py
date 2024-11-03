import pygame
import sys

# Inicializa o Pygame
pygame.init()

# Configura a tela
screen = pygame.display.set_mode((800, 600))

# Cores
day_color = (135, 206, 235)  # Azul claro para o dia (céu)
night_color = (0, 0, 0)  # Preto para a noite
alpha_value = 0  # Valor inicial de transparência

# Tempo (em segundos)
day_length = 1  # Duração do dia
night_length = 1  # Duração da noite
total_cycle = day_length + night_length

# Filtro noturno
night_filter = pygame.Surface((800, 600))
night_filter.fill(night_color)
night_filter.set_alpha(alpha_value)  # Define a transparência inicial

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Atualiza o tempo
    time_passed = pygame.time.get_ticks() / 1000 % total_cycle  # Tempo em segundos

    # Define a transparência do filtro com base no tempo
    if time_passed < day_length:
        alpha_value = 0  # Dia (sem filtro)
    else:
        # Cálculo da transparência durante a noite
        night_time = time_passed - day_length
        alpha_value = int((night_time / night_length) * 255)  # Aumenta a transparência até 255

    night_filter.set_alpha(alpha_value)  # Atualiza a transparência do filtro

    # Desenha o fundo
    screen.fill(day_color)  # Céu durante o dia
    screen.blit(night_filter, (0, 0))  # Aplica o filtro noturno

    pygame.display.flip()  # Atualiza a tela
    clock.tick(60)  # Limita a 60 FPS
