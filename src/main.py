import pygame
from UI.UI import *
from actors.player import *


pygame.init()

screen = pygame.display.set_mode((1450, 830))
clock = pygame.time.Clock()


player = Player(
    name="Flavio",
    sprite='assets/player.png',
    position=(100, 100),
    size=(70, 100)
)
enti = []

Ui = UI(screen)
hud = HUD(
    screen= screen,
    player= player
)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((20, 120, 20))   

    keys = pygame.key.get_pressed()
    player.move(keys)  
    if player._Max_STM > player.STM:
        player.STM += 0.05

    
    Ui.draw_sprite(
        entity=player
    )
    
    Ui.update(
        entities= enti
    ) 
    hud.draw()
    pygame.display.flip() 
    clock.tick(60)  

pygame.quit()
