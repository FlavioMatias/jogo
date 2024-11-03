import pygame

from .settings import Settings

class World:
    def __init__(self):
        self.camera = pygame.Rect(0, 0, Settings.screen_width, Settings.screen_height)
        self.size = None
        
