class Player:
    def __init__(self):
        self.largura = 50
        self.altura = 50
        self.rect = pygame.Rect(LARGURA // 2 - self.largura // 2, ALTURA // 2 - self.altura // 2, self.largura, self.altura)
        self.velocidade = 10
        self.sprites_direita = sprites_direita  # lista de sprites para andar à direita
        self.sprites_esquerda = sprites_esquerda  # lista de sprites para andar à esquerda
        self.sprite_atual = self.sprites_direita[0]  # sprite inicial
        self.frame_atual = 0  # Contador de frames
        self.frame_rate = 5  # Controle da taxa de troca de frames

    def mover(self, teclas):
        """Move o jogador de acordo com as teclas pressionadas e atualiza a animação."""
        movendo = False
        if teclas[pygame.K_LEFT]:
            self.rect.x -= self.velocidade
            movendo = True
            self.sprite_atual = self.sprites_esquerda[self.frame_atual // self.frame_rate]
        if teclas[pygame.K_RIGHT]:
            self.rect.x += self.velocidade
            movendo = True
            self.sprite_atual = self.sprites_direita[self.frame_atual // self.frame_rate]
        if teclas[pygame.K_UP]:
            self.rect.y -= self.velocidade
        if teclas[pygame.K_DOWN]:
            self.rect.y += self.velocidade

        # Atualiza o contador de frames se o jogador estiver se movendo
        if movendo:
            self.frame_atual += 1
            if self.frame_atual >= len(self.sprites_direita) * self.frame_rate:
                self.frame_atual = 0  # Reseta o contador de frames

    def desenhar(self, tela, camera):
        """Desenha o jogador na tela com o sprite atual."""
        tela.blit(self.sprite_atual, (self.rect.x - camera.x, self.rect.y - camera.y))

# No loop principal do jogo:
ui.desenhar(screen, player, bloco_amarelo, inimigo, camera)
player.desenhar(screen, camera)  # Chame o método de desenhar do jogador
