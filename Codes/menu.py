import pygame
"""
Arquivo com funções relacionadas ao menu do jogo.
"""

def escrever(string, tela, fonte, cor, x, y, tamanho):
    """
    Função que escreve uma mensagem na tela do jogo
    """
    font = pygame.font.SysFont(fonte, tamanho, True, True)
    texto = font.render(string, True, cor)
    tela.blit(texto, (x, y))
    pygame.display.flip()


def posicionar_seta(seletor, screen):

    seta = pygame.image.load(".\imagens-de-fundo\-seta.png")
    match seletor:
        case 1:
            screen.blit(seta, (425, 255))
        case 2:
            screen.blit(seta, (425, 282))
        case 3:
            screen.blit(seta, (425, 307))
        case 4:
            screen.blit(seta, (425, 332))
        case 5:
            screen.blit(seta, (425, 357))



