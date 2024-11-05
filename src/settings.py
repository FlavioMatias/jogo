import pygame

class GameSettings:
    def __init__(self):
        pygame.init()
        self.screen_width = 1300
        self.screen_height = 800
        self.world_size = (10000, 10000)
        self.title = "name"
        self.background = self.sprite = pygame.image.load("assets/background.png")
        self.fps = 60
        self.fullscreen = True
        
    def create_screen(self):
        """Cria a tela no modo correto (janela ou fullscreen)."""
        if self.fullscreen:
            return pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
        else:
            return pygame.display.set_mode((self.screen_width, self.screen_height))

    def toggle_fullscreen(self, screen):
        """Alterna entre tela cheia e modo janela e recria a tela."""
        self.fullscreen = not self.fullscreen
        screen = self.create_screen() 
        
 
Settings = GameSettings()