import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pygame
from UI.UI import *
from actors.player import Player
from actors.animals import Mob
from .game import World
from random import randint
from structure.vegetation import Carvalho

world = World()
Ui = UI()

player = Player(
    name="Flavio",
    sprite='assets/player.png',
    position=(500, 500),
    size=(70, 100)
)
coelho = Mob(
    player= player
)
arvore = Carvalho(
    position=(randint(100, 1000), randint(100, 1000))
)
hud = HUD(
    screen= Ui.screen,
    player= player
)


enti = []
structure = []
enti.append(coelho)
enti.append(player)
structure.append(arvore)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    Ui.screen.fill((64, 200, 208))  

    keys = pygame.key.get_pressed()
    mouse_buttons = pygame.mouse.get_pressed()
    
    player.atack(mouse_buttons)
    player.move(keys, world.camera)

    Ui.draw_backgroud(
        camera=world.camera
    )
    
    player.player_recover(
        keymouse=mouse_buttons,
        key=keys
        )
    
    
    Ui.update_entities(
        entities=enti,
        camera=world.camera,
        player=player
        
    )
    Ui.update_structures(
        structures= structure,
        entities=enti,
        camera=world.camera
    )
    Ui.screen.blit(pygame.image.load("night.png"),(0,0))
    hud.draw(world.camera)
    
    pygame.display.flip()  
    pygame.time.Clock().tick(Settings.fps)

pygame.quit()
