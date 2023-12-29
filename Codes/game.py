import pygame
from menu import *
from random import randint

player_img = pygame.image.load(".\imagens\cj-normal.png")
player_shooting_img = pygame.image.load('.\imagens\cj-atirando.png')
tiro_img = pygame.image.load(".\imagens\-bala-direita.png")

"""
Arquivo com funções usadas enquanto o jogo roda.
"""

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
    elif element == 'F':
        cor = (0, 0, 100)

    return cor

def desenhar(screen, cor, x, y, size):
    """"
    Função que desenha um elemento específico na tela do jogo
    """
    pygame.draw.rect(screen, cor, (x * size,
    y * size, size, size))

def desenhar_img(element, x, y, screen, size, player=player_img, tiro=tiro_img, player_shooting=player_shooting_img):
    x *= size
    y *= size
    if element == '+':
        screen.blit(player, (x,y))
    elif element == '>':
        screen.blit(tiro, (x, y))
    elif element == '++':
        screen.blit(player_shooting, (x, y))

     
def mostrar_matriz(matriz, altura, largura, tela, tamanho, pont, energ, fonte):
    """
    Função que desenha todo o jogo na tela
    """
    tela.fill((255, 255, 255))

    for i in range(0, altura):
        for j in range(0, largura):
            desenhar_img(matriz[i][j], j, i, tela, tamanho)

    escrever(f'Energia: {energ}', tela, fonte, (0,0,0), 3, 0, tamanho)
    escrever(f'Pontuação: {pont}', tela, fonte, (0,0,0), 600, 0, tamanho)
    pygame.display.flip()

def mover_objetos(matriz, altura, largura, pont, energ):
    """
    função que move os objetos presentes no jogo(inimigos, balas e combustível)
    """

    # movimentação dos tiros
    i = 0
    j = 0
    while i < altura:
        while j < largura:
            if matriz[i][j] == '>':
                    if j < (largura - 1):
                        if matriz[i][j + 1] == ' ':
                            matriz[i][j + 1] = '>'
                            matriz[i][j] = ' '
                            j += 1

                        elif matriz[i][j + 1] == 'X' or matriz[i][j + 1] == 'F':
                            if matriz[i][j + 1] == 'X':
                                 pont += 50
                            matriz[i][j + 1] = ' '
                            matriz[i][j] = ' '

                    elif j == (largura - 1):
                        matriz[i][j] = ' '

            j += 1
        j = 0
        i += 1

    # movimentação dos inimigos e do combustível
    i = 0
    j = 0
    while i < altura:
        while j < largura:
            if matriz[i][j] == 'X':
                    if j > 0:
                        if matriz[i][j - 1] == ' ':
                            matriz[i][j - 1] = 'X'
                            matriz[i][j] = ' '
                            j += 1

                        elif matriz[i][j - 1] == '+': # morte do player
                            matriz[i][j - 1] = ' '
                            matriz[i][j] = ' '

                    elif j == 0:
                        matriz[i][j] = ' '
            elif matriz[i][j] == 'F':
                    if j > 0:
                        if matriz[i][j - 1] == ' ':
                            matriz[i][j - 1] = 'F'
                            matriz[i][j] = ' '
                            j += 1
                        elif matriz[i][j - 1] == '+': # aumento do combustivel
                            energ += 40
                            matriz[i][j] = ' '
                            j += 1
                    elif j == 0:
                        matriz[i][j] = ' '
            j += 1
        j = 0
        i += 1

    # retorno da matriz e dos valores da energia e pontuação após a movimentação    
    return matriz, pont, energ

def spawn(matriz, objeto, prob, limpar, qtde_max):
    """
    Função que spawna aleatoriamente inimigos ou combustível no mapa
    OBS: chance em porcentagem
    """
    b = randint(0, 100) 
    if b <= prob:
        qtde = randint(0, qtde_max) # qtde de inimigos que vão aparecer
        
        if qtde > 0:
                usadas = []
                for i in range(0, qtde):
                    while True:
                        y = randint(0, 9)

                        if y not in usadas:
                            matriz[y][134] = objeto 
                            usadas.append(y)
                            break
                if limpar:
                    del usadas

def limpar_matriz(grid, h, l):
     """
     Função para a limpeza da matriz para o possível início
     de uma futura partida
     """
     for i in range(0, h):
          for j in range(0, l):
               grid[i][j] = ' '

def resetar_contador(c, e):
    """
    Função que reseta o contador de segundos a cada segundo
    e diminui a energia do personagem em 1.
    """
    if c == 20:
        c = 0 # reseta o contador
        e -= 1 # diminuição da energia do personagem a cada frame
    return c, e