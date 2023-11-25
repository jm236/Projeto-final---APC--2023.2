from functions import *
import pygame

#  definição das variaveis utilizadas no jogo
nome_do_jogo = 'GTA VII'
aviso_um = 'Bem vindo! Pressione Enter para continuar'
fonte = "Monospace"

fps = 20 # fps do jogo
enter = 13 # codigo do enter no pygame
inicio = True # variavel que indica que o jogo ainda esta na tela inicial 
menu_inicial = False # variavel que indica se o jogo esta no menu 
playing = False # variavel que indica se o jogo ta rodando

tam_jogo = 15
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
enemy = 'X'
comb = 'F'
bala = '>'

# energia inicial do personagem
energ = 400

# pontuação do jogador
pont = 0

# coordenadas do player
player_x = 1
player_y = 5
matriz[player_y][player_x] = '+'


pygame.init()

# configuracao do fps
clock = pygame.time.Clock()

screen = pygame.display.set_mode((altura_menu, largura_menu)) # tamanho da tela inicial
pygame.display.set_caption("GTA VII")

# escrita da msg inicial ao abrir o jogo
escrever(nome_do_jogo, screen, fonte, vermelho, 200, 135, tam_menu * 10)
escrever(aviso_um, screen, fonte, branco, 180, 250, tam_menu * 2)
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
                    screen.fill(preto)
                    menu(screen, tam_menu, largura_menu, altura_menu) # função que apresentará o menu inicial do game
                    pygame.display.flip()

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

    if playing: # quando o jogo está rodando
        #movimentação dos objetos e atualização dos frames
        mover_objetos(matriz, altura_jogo, largura_jogo, energ) 
        mostrar_matriz(matriz, altura_jogo, largura_jogo,tela_jogo, tam_jogo)
        
        escrever(f'Energia: {energ}', tela_jogo, fonte, preto, 3, 0, tam_jogo)
        escrever(f'Pontuação: {pont}', tela_jogo, fonte, preto, 600, 0, tam_jogo)

        # spawn de inimigos e combustível
        spawn(matriz, enemy)
        spawn(matriz, comb)

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
                
                elif event.key == pygame.K_t: # geração do tiro
                    bala_y = player_y
                    bala_x = player_x + 1
                    matriz[bala_y][bala_x] = bala
                    energ -= 3

    clock.tick(fps)


pygame.quit()

