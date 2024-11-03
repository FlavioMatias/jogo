import pygame

class GameSettings:
    def __init__(self):
        self.screen_width = 1450
        self.screen_height = 830
        self.world_size = (10000, 10000)
        self.title = "name"
        self.background = self.sprite = pygame.image.load("assets/background.png")
        self.fps = 60
        self.fullscreen = True  

    def toggle_fullscreen(self):
        """Alterna entre tela cheia e modo janela."""
        self.fullscreen = not self.fullscreen
        
    
 
 
Settings = GameSettings()