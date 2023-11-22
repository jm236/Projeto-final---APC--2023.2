import pygame

def escrever(string, tela, fonte, cor, x, y, tamanho):
    """
    Função que escreve uma mensagem na tela do jogo
    """
    font = pygame.font.SysFont(fonte, tamanho, True, True)
    texto = font.render(string, True, cor)
    tela.blit(texto, (x, y))

def config_fps(fps):
    """
    Definição do FPS do game
    """
    clock = pygame.time.Clock()
    clock.tick(fps)
