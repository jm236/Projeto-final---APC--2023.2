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
