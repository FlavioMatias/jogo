import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pygame
from UI.UI import *
from actors.player import Player
from actors.animals import Mob
from .game import World, gerate_carvalho, day_cicle
from random import randint
from structure.vegetation import Carvalho

world = World()
Ui = UI()
enti = []
structure = []

player = Player(
    name="Player",
    sprite='assets/player.png',
    position=(700, 500),
    size=(70, 100)
)

hud = HUD(
    screen= Ui.screen,
    player= player
)


coelho = Mob(
player= player
)
enti.append(coelho)


enti.append(player)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F11:
                Ui.change_screen()
    
    Ui.screen.fill((64, 200, 228))  

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
    day_cicle(Ui.screen)
    hud.draw(world.camera)
    
    pygame.display.flip()  
    pygame.time.Clock().tick(Settings.fps)

pygame.quit()
