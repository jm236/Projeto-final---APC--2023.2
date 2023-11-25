import pygame

def escrever(string, tela, fonte, cor, x, y, tamanho):
    """
    Função que escreve uma mensagem na tela do jogo
    """
    font = pygame.font.SysFont(fonte, tamanho, True, True)
    texto = font.render(string, True, cor)
    tela.blit(texto, (x, y))

def menu(tela, tam, largura, altura):
    """"
    Função que apresenta o menu inicial na tela
    """
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
    """
    Função que escolhe a cor de acordo com o elemento do jogo (inimigo, jogador, bala ou combustível)
    """
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
    """"
    Função que desenha um elemento específico na tela do jogo
    """
    pygame.draw.rect(screen, cor, (x * size,
    y * size, size, size))

def mostrar_matriz(matriz, altura, largura, tela, tamanho):
    """
    Função que desenha todo o jogo na tela
    """
    tela.fill((255, 255, 255))

    for i in range(0, altura):
        for j in range(0, largura):
                    desenhar(tela, escolhe_cor(matriz[i][j]), j, i, tamanho) # desenho

    pygame.display.flip()

def mover_objetos(matriz, altura, largura):
    """
    função que move os objetos presentes no jogo(inimigos, balas e combustível)
    """
    i = 0
    j = 0
    while i < altura:
        while j < largura:
            if matriz[i][j] == '>':
                    if j < (largura - 1):
                        matriz[i][j + 1] = '>'
                        matriz[i][j] = ' '
                        j += 1
                    elif j == (largura - 1):
                        matriz[i][j] = ' '
            j += 1
        j = 0
        i += 1




