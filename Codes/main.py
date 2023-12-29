from menu import *
from game import *
from gameover import *
from time import sleep
import pygame

#  definição das variaveis utilizadas no jogo
nome_do_jogo = 'GTA VII'
fonte = "monospace"

fps = 20 # fps do jogo
contador = 0 # contador que aumenta a cada frame, quando chega em 20 o combustivel diminui
enter = 13 # codigo do enter no pygame
inicio = True # variavel que indica que o jogo ainda esta na tela inicial 
menu_inicial = False # variavel que indica se o jogo esta no menu 
playing = False # variavel que indica se o jogo ta rodando
game_overI = False # variavel que indica se o jogo esta na tela de game over
game_overII = False
instrucoes = False
paused = False

tam_jogo = 20
largura_jogo = 135
altura_jogo = 10
tam_menu = 5 # tamanho da tela
largura_menu = 72 * tam_menu
altura_menu = 128 * tam_menu

# Lista bidimensional para armazenar objetos em movimento
matriz = [[' ' for _ in range(largura_jogo)] for _ in range(altura_jogo)]

# cores utilizadas 
vermelho = (255, 0, 0)
branco = (255, 255, 255)
preto = (0, 0, 0)
verde = (0, 255, 0)
azul = (0, 0, 255)
verde_esc = (0, 100, 0)

# Definição de objetos no jogo
player = '+'
player_atirando = '++'
enemy = 'X'
comb = 'F'
bala = '>'

# energia inicial do personagem
energ = 400

#probabilidades de serem gerados
prob_enemies = 25
prob_fuel = 5

# variavel usada na animacao do cj atirando
duracao_animacao = -1

# pontuação do jogador
pont = 0

# coordenadas iniciais do player
player_x = 1
player_y = 5
matriz[player_y][player_x] = '+'


pygame.init()

# configuracao do fps
clock = pygame.time.Clock()

screen = pygame.display.set_mode((altura_menu, largura_menu)) # tamanho da tela inicial
pygame.display.set_caption(nome_do_jogo)

# escrita da msg inicial ao abrir o jogo
escrever(nome_do_jogo, screen, fonte, vermelho, 200, 135, tam_menu * 10)
escrever('Bem vindo! Pressione Enter para continuar', screen, fonte, branco, 180, 250, tam_menu * 2)
pygame.display.flip()

running = True
while running:

    # loop para eventos no jogo
    if inicio: # quando esta no inicio do jogo
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # pygame.QUIT event means the user clicked X to close your window
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == 13:
                    inicio, menu_inicial = False, True # o jogo nao esta mais no inicio
                    menu(screen, tam_menu, largura_menu, altura_menu, fonte) # função que apresentará o menu inicial do game

    if menu_inicial: # quando está no menu inicial
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # pygame.QUIT event means the user clicked X to close your window
                running = False    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_5: # 5 pra sair
                    running = False

                elif event.key == pygame.K_1: # 1 pra jogar
                    playing, menu_inicial = True, False
                    tela_jogo = pygame.display.set_mode((largura_jogo * tam_jogo, altura_jogo * tam_jogo))

                elif event.key == pygame.K_4:
                    instrucoes, menu_inicial = True, False
                    mostrar_instrucoes(altura_menu, largura_menu, preto, branco, tam_menu, fonte)

                elif event.key == pygame.K_6:
                    menu_inicial, teste = False, True
                    tela_jogo = pygame.display.set_mode((largura_jogo * tam_jogo, altura_jogo * tam_jogo))

    if instrucoes:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # pygame.QUIT event means the user clicked X to close your window
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == 13:
                    menu_inicial, instrucoes = True, False # o jogo nao esta mais no inicio
                    menu(screen, tam_menu, largura_menu, altura_menu, fonte) # função que apresentará o menu inicial do game



    if playing: # quando o jogo está rodando

        contador, energ = resetar_contador(contador,energ) # reset do contador e da energia
        if duracao_animacao > 0:
            duracao_animacao -= 1
        elif duracao_animacao == 0:
            matriz[player_y][player_x] = player
            duracao_animacao = -1 
        
        #movimentação dos objetos e atualização dos frames
        matriz, pont, energ = mover_objetos(matriz, altura_jogo, largura_jogo, pont, energ)

        # verificação da morte do personagem e do motivo dela 
        morte = morreu(matriz, energ, player_y)
        motivo = motivo_morte(morte)
        if 'sim' in morte:
            game_overI, playing = True, False # encerramento da partida em caso de morte do jogador

        mostrar_matriz(matriz, altura_jogo, largura_jogo,tela_jogo, tam_jogo, pont, energ, fonte)
        contador += 1

        # spawn de inimigos e combustível
        spawn(matriz, enemy, prob_enemies, False, 4)
        spawn(matriz, comb, prob_fuel, True, 2)

        for event in pygame.event.get():
            if event.type == pygame.QUIT: # pygame.QUIT event means the user clicked X to close your window
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP: # movimentação do personagem para cima
                    if player_y > 0:    
                        matriz[player_y][player_x] = ' '
                        matriz[player_y - 1][player_x] = player
                        player_y -= 1
                        energ -= 2

                elif event.key == pygame.K_DOWN: # movimentação do personagem para baixo
                    if player_y < 9:    
                        matriz[player_y][player_x] = ' '
                        matriz[player_y + 1][player_x] = player
                        player_y += 1
                        energ -= 2
                
                elif event.key == pygame.K_SPACE: # geração do tiro
                    bala_y = player_y
                    bala_x = player_x + 1
                    matriz[bala_y][bala_x] = bala
                    matriz[player_y][player_x] = player_atirando
                    duracao_animacao = 6 # indica qtos frames a imagem do cj atirando vai ficar
                    energ -= 3

                elif event.key == pygame.K_p:
                    paused, playing = True, False
                
                elif event.key == 13: # Enter dropa do jogo
                    menu_inicial = True
                    playing = False

                    # reset das configs do jogo para uma futura partida
                    contador, energ, pont = 0, 400, 0
                    limpar_matriz(matriz, altura_jogo, largura_jogo)
                    player_x, player_y = 1, 5
                    matriz[player_y][player_x] = '+'
                    screen = pygame.display.set_mode((altura_menu, largura_menu))
                    menu(screen, tam_menu, largura_menu, altura_menu, fonte) # função que apresentará o menu inicial do game
                    pygame.display.flip()


    if game_overI:
        tela_morte(largura_menu, altura_menu, fonte, tam_menu, pont, motivo)
        
        # reset das configs do jogo para uma futura partida
        contador, energ, pont = 0, 400, 0
        limpar_matriz(matriz, altura_jogo, largura_jogo)
        player_x, player_y = 1, 5
        matriz[player_y][player_x] = '+'
        game_overI, game_overII = False, True

    if game_overII:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # pygame.QUIT event means the user clicked X to close your window
                running = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == 13:
                    game_over, menu_inicial = False, True # o jogo nao esta mais no inicio
                    menu(screen, tam_menu, largura_menu, altura_menu, fonte) # função que apresentará o menu inicial do game
                    pygame.display.flip()

    if  paused:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused, playing = False, True

                elif event.key == 13: # Enter dropa do jogo
                    menu_inicial = True
                    playing = False

                    # reset das configs do jogo para uma futura partida
                    contador, energ, pont = 0, 400, 0
                    limpar_matriz(matriz, altura_jogo, largura_jogo)
                    player_x, player_y = 1, 5
                    matriz[player_y][player_x] = '+'
                    screen = pygame.display.set_mode((altura_menu, largura_menu))
                    menu(screen, tam_menu, largura_menu, altura_menu, fonte) # função que apresentará o menu inicial do game
                    pygame.display.flip()


        
    clock.tick(fps)
    
pygame.quit()
