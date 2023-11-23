import pygame
import random
import sys

# Inicialização do Pygame
pygame.init()

# Configurações do jogo
WIDTH, HEIGHT = 135, 10
GRID_SIZE = 20
FPS = 20

# Cores
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
DARK_GREEN = (0, 100, 0)

# Definição de objetos no jogo
PLAYER = '+'
ENEMY = 'X'
FUEL = 'F'
BULLET = '>'

# Inicialização do jogador
player_row = HEIGHT // 2
player_col = 0
player_fuel = 400
player_score = 0

# Lista bidimensional para armazenar objetos em movimento
grid = [[' ' for _ in range(WIDTH)] for _ in range(HEIGHT)]

# Inicialização da tela
screen = pygame.display.set_mode((WIDTH * GRID_SIZE, HEIGHT * GRID_SIZE))
pygame.display.set_caption("Jogo 2D - Bem-vindo!")

# Função para desenhar o grid
def draw_grid():
    for row in range(HEIGHT):
        for col in range(WIDTH):
            pygame.draw.rect(screen, WHITE, (col * GRID_SIZE, row * GRID_SIZE, GRID_SIZE, GRID_SIZE), 1)

# Função para desenhar o jogador e objetos
def draw_objects():
    for row in range(HEIGHT):
        for col in range(WIDTH):
            obj = grid[row][col]
            color = GREEN if obj == PLAYER else RED if obj == ENEMY else BLUE if obj == FUEL else DARK_GREEN
            pygame.draw.rect(screen, color, (col * GRID_SIZE, row * GRID_SIZE, GRID_SIZE, GRID_SIZE))

# Função para mover os objetos
def move_objects():
    global player_row, player_col, player_fuel, player_score

    # Mover jogador
    grid[player_row][player_col] = ' '

    if pygame.key.get_pressed()[pygame.K_UP] and player_row > 0:
        player_row -= 1
        player_fuel -= 2
    elif pygame.key.get_pressed()[pygame.K_DOWN] and player_row < HEIGHT - 1:
        player_row += 1
        player_fuel -= 2
    elif pygame.key.get_pressed()[pygame.K_SPACE] and player_fuel >= 3:
        grid[player_row][player_col + 1] = BULLET
        player_fuel -= 3
    else:
        player_fuel -= 1

    grid[player_row][player_col] = PLAYER

    # Mover objetos inimigos e de combustível
    for row in range(HEIGHT):
        for col in range(WIDTH):
            obj = grid[row][col]
            if obj == ENEMY:
                grid[row][col] = ' '
            elif obj == FUEL:
                grid[row][col] = ' '

    if random.randint(0, 10) < 3:
        row = random.randint(0, HEIGHT - 1)
        grid[row][WIDTH - 1] = random.choice([ENEMY, FUEL])

    # Verificar colisões
    if grid[player_row][player_col] == ENEMY:
        game_over("Atingido por um inimigo!")

    # Verificar se o tiro atingiu um inimigo
    for col in range(player_col + 1, WIDTH):
        if grid[player_row][col] == BULLET:
            if grid[player_row][col + 1] == ENEMY:
                grid[player_row][col] = ' '
                grid[player_row][col + 1] = ' '
                player_score += 50

    # Verificar se o tiro ultrapassou o limite direito do grid
    for row in range(HEIGHT):
        if grid[row][WIDTH - 1] == BULLET:
            grid[row][WIDTH - 1] = ' '

    # Verificar se o jogador ficou sem combustível
    if player_fuel <= 0:
        game_over("Combustível esgotado!")

# Função para encerrar o jogo
def game_over(message):
    global player_score
    print("GAME OVER")
    print(message)
    print(f"Pontuação final: {player_score}")
    pygame.quit()
    sys.exit()

# Loop principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    move_objects()

    # Limpar a tela
    screen.fill((0, 0, 0))

    draw_grid()
    draw_objects()

    # Atualizar a tela
    pygame.display.flip()

    # Controlar a taxa de quadros por segundo
    pygame.time.Clock().tick(FPS)

# Encerrar o Pygame
pygame.quit()
