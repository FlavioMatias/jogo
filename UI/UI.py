import pygame
from src.settings import Settings

class UI:
    def __init__(self):
        self.screen = self.__game_init()
        self.font = pygame.font.Font(None, 24)


    def __game_init(self):
        """Inicializa o Pygame e configura a tela do jogo."""
        pygame.init()
        tela = pygame.display.set_mode((Settings.screen_width, Settings.screen_height))  # Cria a tela do jogo
        pygame.display.set_caption("Player na Tela")  # Define o título da janela
        return tela
    
    def __move_entities(self, entities, player):
        for mobs in entities:
            if mobs != player:
                mobs.move()
                
    def draw_backgroud(self, camera):
        self.screen.blit(Settings.background, (-camera.x, -camera.y))
        

    def __draw_entity(self, entity, camera):
        """ Renderiza o sprite de uma entidade na posição atual """
        if entity.alive:
            self.screen.blit(entity.sprite, (entity.rect.x - camera.x, entity.rect.y - camera.y))
            
            
    def update_entities(self, entities : list, camera, player):
        """Desenha o fundo e todas as entidades do jogo na tela, considerando a posição da câmera."""
        
        self.__move_entities(entities, player)
        
        for entity in entities:
            self.__draw_entity(entity, camera)
            
    def update_structures(self, structures : list, entities : list, camera):
        """Desenha o fundo e todas as entidades do jogo na tela, considerando a posição da câmera."""
        
        self.__colision_check(structures, entities)
        
        for entity in structures:
            self.screen.blit(entity.sprite, (entity.rect.x - camera.x, entity.rect.y - camera.y))
            
    def __colision_check(self, structures, entities):
        for elements in structures:
            elements.check_collision(entities)
                
            
            
            
class HUD:
    def __init__(self, screen, player: object, font_size=15):
        self.__screen = screen
        self.__player = player
        self.__font = pygame.font.Font("assets/font/PressStart2P.ttf", font_size)  

    def draw(self, camera):
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
            font = pygame.font.Font("assets/font/PressStart2P.ttf", 15)
            text_surface = font.render(name, True, WHITE)
            self.__screen.blit(text_surface, (10 + bar_width + 10, bar_y))
        self.draw_player_name(camera)
        self.draw_mira()
    def draw_player_name(self, camera):
        """Desenha o nome do jogador acima do sprite, considerando a posição da câmera."""
        name_surface = self.__font.render(self.__player.nick, True, (255, 255, 255)) 
        # Ajuste a posição para incluir a posição da câmera
        name_x = (self.__player.rect.centerx - camera.x) - name_surface.get_width() // 2  
        name_y = (self.__player.rect.top - camera.y) - name_surface.get_height() - 5
        self.__screen.blit(name_surface, (name_x, name_y))
        
    def draw_mira(self):
        mauseXY = pygame.mouse.get_pos()  
        pygame.mouse.set_visible(False)
        sprite = pygame.image.load("assets/MIRA-removebg-preview.png")
        sprite = pygame.transform.scale(sprite, (20,20))
        self.__screen.blit(sprite, mauseXY)

        

