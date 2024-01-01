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

def menu(tela, tam, largura, altura, fonte):
    """"
    Função que apresenta o menu inicial na tela
    """
    nome_do_jogo = 'GTA VII'
    vermelho = (255, 0, 0)
    branco = (255, 255, 255)
    preto = (0, 0, 0)
    tela.fill(preto)
    
    escrever(nome_do_jogo, tela, fonte, vermelho, 160, 40, tam * 10)

    string = "1- Jogar"
    escrever(string, tela, fonte, branco, (largura // 2),((altura // 4) - 40), tam * 3)   

    string = "2- Configurações(Ainda não implementado!)" 
    escrever(string, tela, fonte, branco, (largura // 2),((altura // 4) - 20), tam * 3)  

    string = "3- Ranking(Ainda não implementado!)" 
    escrever(string, tela, fonte, branco, (largura // 2),((altura // 4)), tam * 3) 

    string = "4- Instruções" 
    escrever(string, tela, fonte, branco, (largura // 2),((altura // 4) + 20), tam * 3)

    string = "5- Sair" 
    escrever(string, tela, fonte, branco, (largura // 2),((altura // 4) + 40), tam * 3)  
    
    pygame.display.flip()

def mostrar_instrucoes(h, l, corI, corII, tam, fonte): 
    """
    Função que apresenta a tela de instruções.
    """   
    screen = pygame.display.set_mode((l, h))
    screen.fill(corI)

    string = 'Para se movimentar para cima ou para baixo' 
    escrever(string, screen, fonte, corII, (h // 8), (l // 8)+20, tam * 3)
    
    string = 'e desviar dos inimigos, utilize as setas;'
    escrever(string, screen, fonte, corII, (h // 8), (l // 8)+40, tam * 3)

    string = 'Para atirar em seus inimigos e não ser'
    escrever(string, screen, fonte, corII, (h // 8), (l // 8)+60, tam * 3)

    string = 'atacado, aperte espaço;'
    escrever(string, screen, fonte, corII, (h // 8), (l // 8)+80, tam * 3)

    string = 'Lembre-se que atirar ou se movimentar custam'
    escrever(string, screen, fonte, corII, (h // 8), (l // 8)+100, tam * 3)

    string = 'respectivamente 3 e 2 pontos de energia;'
    escrever(string, screen, fonte, corII, (h // 8), (l // 8)+120, tam * 3)

    string = 'Matar um inimigo aumenta sua pontuação em 50 pontos;'
    escrever(string, screen, fonte, corII, (h // 8), (l // 8)+140, tam * 3)

    string = 'Sempre colete pontos de energia, pois'
    escrever(string, screen, fonte, corII, (h // 8), (l // 8)+160, tam * 3)

    string = 'ela pode acabar uma hora;'
    escrever(string, screen, fonte, corII, (h // 8), (l // 8)+180, tam * 3)

    string = 'Faça o máximo de pontos que conseguir e divirta-se!'
    escrever(string, screen, fonte, corII, (h // 8), (l // 8)+200, tam * 3)

    string = 'Caso queira pausar uma partida, aperte P. Já para sair,'
    escrever(string, screen, fonte, corII, (h // 8), (l // 8)+220, tam * 3)

    string = 'aperte Enter'
    escrever(string, screen, fonte, corII, (h // 8), (l // 8)+240, tam * 3)

    string = 'Assim que tiver lido tudo, aperte enter para retornar ao menu.'
    escrever(string, screen, fonte, corII, (h // 8), (l // 8)+260, tam * 3)
    
    pygame.display.flip()