from functions import *
import pygame

#  definição das variaveis utilizadas no jogo
nome_do_jogo = 'GTA VII'
aviso_um = 'Bem vindo! Pressione Enter para continuar'

fps = 30 # fps do jogo
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

# coordenadas do player
player_x = 1
player_y = 5
matriz[player_y][player_x] = '+'


pygame.init()

# configuracao do fps
config_fps(fps)

screen = pygame.display.set_mode((altura_menu, largura_menu)) # tamanho da tela inicial
pygame.display.set_caption("Jogo 2D - Bem-vindo!")

# escrita da msg inicial ao abrir o jogo
escrever(nome_do_jogo, screen, "Monospace", vermelho, 200, 135, tam_menu * 10)
escrever(aviso_um, screen, "Monospace", branco, 180, 250, tam_menu * 2)

pygame.display.flip()

running = True
while running:
    # loop para eventos no jogo
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: # pygame.QUIT event means the user clicked X to close your window
            running = False

        if inicio == True:
            if event.type == pygame.KEYDOWN:
                if event.key == 13:
                    inicio, menu_inicial = False, True # o jogo nao esta mais no inicio
                    screen.fill(preto)
                    menu(screen, tam_menu, largura_menu, altura_menu) # função que apresentará o menu inicial do game
                    pygame.display.flip()

        if menu_inicial == True:    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_5: # 5 pra sair
                    running = False

                elif event.key == pygame.K_1: # 1 pra jogar

                    playing, menu_inicial = True, False
                    tela_jogo = pygame.display.set_mode((largura_jogo * tam_jogo, altura_jogo * tam_jogo))
                    tela_jogo.fill(branco)
                    pygame.display.flip()

                    mostrar_matriz(matriz, altura_jogo, largura_jogo, tela_jogo, tam_jogo)                    
                    pygame.display.flip()

        if playing == True:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if player_y > 0:    
                        player_y -= 1
                        desenhar(tela_jogo, verde, player_x, player_y, tam_jogo) # desenho do personagem
                        desenhar(tela_jogo, branco, player_x, player_y + 1, tam_jogo) # desenho do personagem
                        pygame.display.flip()

                elif event.key == pygame.K_DOWN:
                    if player_y < 9:
                        player_y += 1
                        desenhar(tela_jogo, verde, player_x, player_y, tam_jogo) # desenho do personagem
                        desenhar(tela_jogo, branco, player_x, player_y - 1, tam_jogo) # desenho do personagem
                        pygame.display.flip()
                
                elif event.key == pygame.K_t:
                    bala_y = player_y
                    bala_x = player_x + 1
                    matriz[bala_y][bala_x + 1] = bala
                    desenhar(tela_jogo, verde_esc, bala_x, bala_y, tam_jogo) # desenho do personagem
                    pygame.display.flip()

pygame.quit()

