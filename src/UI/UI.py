import pygame

class UI:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 24)


    def draw_sprite(self, entity):
        """ Renderiza o sprite de uma entidade na posição atual """
        if entity.alive:
            self.screen.blit(entity.sprite, entity.rect)
            
    def draw_background(self, sprite : str, sizeXY : tuple):
        pass
    def draw_text(self, text, position, color=(255, 255, 255)):
        """ Exibe texto em uma posição específica """
        text_surface = self.font.render(text, True, color)
        self.screen.blit(text_surface, position)

    def update(self, entities):
        """Atualiza a câmera e renderiza todos os elementos na tela."""
        
        for entity in entities:
            self.draw_sprite(entity)
class HUD:
    def __init__(self, screen, player: object, font_size=24):
        self.__screen = screen
        self.__player = player
        self.__font = pygame.font.Font(None, font_size)  

    def draw(self):
        player_info = [
            ("HP", self.__player.HP, self.__player._Max_Hp),
            ("MP", self.__player.MP, self.__player._Max_MP),
            ("STM", self.__player.STM, self.__player._Max_STM),
        ]
        bar_width = 200
        bar_height = 20
        WHITE = (255, 255, 255)
        RED = (255, 0, 0)
        BLUE = (0, 0, 255)
        YELLOW = (255, 255, 0)
        for i, (name, current, maximum) in enumerate(player_info):
            # Calcular a posição y para a barra
            bar_y = 50 + i * (bar_height + 10)

            # Desenhar a barra de fundo
            pygame.draw.rect(self.__screen, (50, 50, 50), (10, bar_y, bar_width, bar_height))

            # Calcular a largura da barra atual
            current_width = (current / maximum) * bar_width

            # Desenhar a barra de progresso
            if name == "HP":
                pygame.draw.rect(self.__screen, RED, (10, bar_y, current_width, bar_height))
            elif name == "MP":
                pygame.draw.rect(self.__screen, BLUE, (10, bar_y, current_width, bar_height))
            elif name == "STM":
                pygame.draw.rect(self.__screen, YELLOW, (10, bar_y, current_width, bar_height))

            # Desenhar o texto do tipo da barra no topo à direita
            font = pygame.font.Font(None, 24)
            text_surface = font.render(name, True, WHITE)
            self.__screen.blit(text_surface, (10 + bar_width + 10, bar_y))
        self.draw_player_name()
    def draw_player_name(self):
        """Desenha o nome do jogador acima do sprite."""
        name_surface = self.__font.render(self.__player.nick, True, (255, 255, 255)) 
        name_x = self.__player.rect.centerx - name_surface.get_width() // 2  
        name_y = self.__player.rect.top - name_surface.get_height() - 5
        self.__screen.blit(name_surface, (name_x, name_y))
        

