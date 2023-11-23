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

def menu(tela, tam, largura, altura):
    nome_do_jogo = 'GTA VII'
    vermelho = (255, 0, 0)
    branco = (255, 255, 255)
    preto = (0, 0, 0)
    
    escrever(nome_do_jogo, tela, "Monospace", vermelho, 225, 40, tam * 10)

    string = "1- Jogar"
    escrever(string, tela, "Monospace", branco, ((altura // 2) - 60), ((largura // 2) - 40), tam * 3)   

    string = "2- Configurações" 
    escrever(string, tela, "Monospace", branco, ((altura // 2) - 60), ((largura // 2) - 20), tam * 3)  

    string = "3- Ranking" 
    escrever(string, tela, "Monospace", branco, ((altura // 2) - 60), ((largura // 2)), tam * 3) 

    string = "4- Instruções" 
    escrever(string, tela, "Monospace", branco, ((altura // 2) - 60), ((largura // 2) + 20), tam * 3)

    string = "5- Sair" 
    escrever(string, tela, "Monospace", branco, ((altura // 2) - 60), ((largura // 2) + 40), tam * 3)  
    
    pygame.display.flip()

def escolhe_cor(element):
    if  element == ' ':
        cor = (255, 255, 255)
    elif element == '+':
        cor = (0, 255, 0)
    elif element == 'X':
        cor = (255, 0, 0)
    elif element == '>':
        cor = (0, 100, 0)

    return cor

def desenhar(screen, cor, x, y, size):
    pygame.draw.rect(screen, cor, (x * size,
    y * size, size, size))

def mostrar_matriz(matriz, altura, largura, tela, tamanho):
    for i in range(0, altura):
        for j in range(0, largura):
                if matriz[i][j] == '+':
                    desenhar(tela, (0, 255, 0), j, i, tamanho) # desenho do personagem
                elif matriz[i][j] == '>':
                    desenhar(tela, (0, 100, 0), j, i, tamanho) # desenho da bala