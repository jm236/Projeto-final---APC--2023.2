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

def draw_grid(t, tela, altura_jogo=10, largura_jogo=135):
    branco = (255, 255, 255)

    for row in range(altura_jogo):
        for col in range(largura_jogo):
            pygame.draw.rect(tela, branco, (col * t, row * t, t, t), 1)


def draw_objects(grid, altura=10, largura=135):
    
    vermelho = (255, 0, 0)
    branco = (255, 255, 255)
    preto = (0, 0, 0)
    verde = (0, 255, 0)
    azul = (0, 0, 255)
    verde_esc = (0, 100, 0)

    for row in range(altura):
        for col in range(largura):
            obj = grid[row][col]
            color = verde if obj == PLAYER else vermelho if obj == ENEMY else aul if obj == FUEL else verde_esc
            pygame.draw.rect(tela_jogo, color, (col * tam_jogo, row * tam_jogo, tam_jogo, tam_jogo))