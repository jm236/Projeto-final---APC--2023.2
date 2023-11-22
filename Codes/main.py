from functions import *
import pygame

#  definição das variaveis utilizadas no jogo
nome_do_jogo = 'GTA VII'
aviso_um = 'Bem vindo! Pressione Enter para continuar'
tam = 5 # tamanho da tela
fps = 30 # fps do jogo
enter = 13 # codigo do enter no pygame

# cores utilizadas 
vermelho = (255, 0, 0)
branco = (255, 255, 255)
preto = (0, 0, 0)

pygame.init()

# configuracao do fps
config_fps(fps)

screen = pygame.display.set_mode((1280, 720)) # tamanho da tela inicial

# escrita da msg inicial ao abrir o jogo
escrever(nome_do_jogo, screen, "Monospace", vermelho, 400, 270, tam * 20)
escrever(aviso_um, screen, "Monospace", branco, 500, 500, tam * 2)

pygame.display.flip()

running = True
while running:
    # loop para eventos no jogo
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: # pygame.QUIT event means the user clicked X to close your window
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == 13:
                screen.fill(preto)
                menu() # função que apresentará o menu inicial do game
                pygame.display.flip()

