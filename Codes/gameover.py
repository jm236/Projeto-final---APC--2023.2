from menu import *
import pygame
"""
Arquivo com funções de verificação da morte do personagem e 
de criação da tela de game over.
"""

def morreu(matriz, comb, y):
    """
    Retorna se o jogador está morto ou vivo e o motivo da morte, respectivamente
    """
    if '+' in matriz[y] or '++' in matriz[y]:
        if comb <= 0:
            return 'sim gasosa'
        else:
            return 'não'
    else:        
        return 'sim atingido'

def motivo_morte(morte):
     """
     Função que retorna o motivo da morte do jogador.
     """
     if 'sim' in morte: 
            if 'gasosa' in morte:
                return 'Deixou a energia acabar =/'
            else:
                return 'Você foi atingido por um inimigo.'
                        
def tela_morte(l, h, fonte, t, pont, motivo):
    """
    Função que apresenta a tela de game over.
    """
    screen = pygame.display.set_mode((h, l))
    screen.fill((0, 0, 0))

    escrever('GAME OVER', screen, fonte, (255, 0, 0), 175, 50, t * 10)
    escrever(f'Pontuação: {pont} pontos.', screen, fonte, (255, 255, 255), 200, 120, t * 3)
    if motivo == 'Te atingiram, presta mais atenção na próxima':
        escrever(motivo, screen, fonte, (255, 255, 255), 130, 140, t * 3)
    else:
        escrever(motivo, screen, fonte, (255, 255, 255), 170, 140, t * 3)
         
    escrever('Aperte Enter para retornar ao menu.', screen, fonte, (255, 255, 255), 120, 250, t * 4)


    pygame.display.flip()