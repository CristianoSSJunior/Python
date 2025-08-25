# Jogo Tetris melhorado - 25/08/2025
import pygame
import random

pygame.font.init()

# ------------------ VARIÁVEIS GLOBAIS ------------------
s_width = 800
s_height = 700
play_width = 300
play_height = 600
block_size = 30

top_left_x = (s_width - play_width) // 2
top_left_y = s_height - play_height

# ------------------ FORMAS ------------------
S = [['.....',
      '......',
      '..00..',
      '.00...',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '...0.',
      '.....']]

Z = [['.....',
      '.....',
      '.00..',
      '..00.',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '.0...',
      '.....']]

I = [['..0..',
      '..0..',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '0000.',
      '.....',
      '.....',
      '.....']]

O = [['.....',
      '.....',
      '.00..',
      '.00..',
      '.....']]

J = [['.....',
      '.0...',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..00.',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '...0.',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '.00..',
      '.....']]

L = [['.....',
      '...0.',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '..00.',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '.0...',
      '.....'],
     ['.....',
      '.00..',
      '..0..',
      '..0..',
      '.....']]

T = [['.....',
      '..0..',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '..0..',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '..0..',
      '.....']]

shapes = [S, Z, I, O, J, L, T]
shape_colors = [(0, 255, 0), (255, 0, 0), (0, 255, 255),
                (255, 255, 0), (255, 165, 0),
                (0, 0, 255), (128, 0, 128)]


# ------------------ CLASSE PEÇA ------------------
class Piece(object):
    def __init__(self, x, y, shape):
        self.x = x
        self.y = y
        self.shape = shape
        self.color = shape_colors[shapes.index(shape)]
        self.rotation = 0


# ------------------ FUNÇÕES AUXILIARES ------------------
def create_grid(locked_positions={}):
    grid = [[(0, 0, 0) for _ in range(10)] for _ in range(20)]
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if (x, y) in locked_positions:
                grid[y][x] = locked_positions[(x, y)]
    return grid


def convert_shape_format(shape):
    positions = []
    format = shape.shape[shape.rotation % len(shape.shape)]
    for i, line in enumerate(format):
        for j, column in enumerate(list(line)):
            if column == '0':
                positions.append((shape.x + j - 2, shape.y + i - 4))
    return positions


def valid_space(shape, grid):
    accepted_positions = [(x, y) for y in range(20)
                          for x in range(10) if grid[y][x] == (0, 0, 0)]
    formatted = convert_shape_format(shape)
    for pos in formatted:
        x, y = pos
        if x < 0 or x >= 10 or y >= 20:
            return False
        if (x, y) not in accepted_positions and y >= 0:
            return False
    return True


def check_lost(locked_positions):
    for x, y in locked_positions:
        if y < 1:
            return True
    return False


def get_shape():
    return Piece(5, 0, random.choice(shapes))


def draw_text_middle(text, size, color, surface):
    font = pygame.font.SysFont('comicsans', size, bold=True)
    label = font.render(text, 1, color)
    surface.blit(label, (top_left_x + play_width/2 - label.get_width()/2,
                         top_left_y + play_height/2 - label.get_height()/2))


def draw_grid(surface, grid):
    sx, sy = top_left_x, top_left_y
    for i in range(len(grid)):
        pygame.draw.line(surface, (128, 128, 128),
                         (sx, sy + i*30), (sx + play_width, sy + i*30))
        for j in range(len(grid[i])):
            pygame.draw.line(surface, (128, 128, 128),
                             (sx + j*30, sy), (sx + j*30, sy + play_height))


def clear_rows(grid, locked):
    inc = 0
    ind = -1
    for i in range(len(grid)-1, -1, -1):
        if (0, 0, 0) not in grid[i]:
            inc += 1
            ind = i
            for j in range(len(grid[i])):
                try:
                    del locked[(j, i)]
                except:
                    continue
    if inc > 0:
        for key in sorted(list(locked), key=lambda x: x[1])[::-1]:
            x, y = key
            if y < ind:
                locked[(x, y+inc)] = locked.pop(key)
    return inc


def draw_next_shape(shape, surface):
    font = pygame.font.SysFont('comicsans', 30)
    label = font.render('Next', 1, (255, 255, 255))
    sx = top_left_x + play_width + 50
    sy = top_left_y + 100
    surface.blit(label, (sx+10, sy-30))

    format = shape.shape[shape.rotation % len(shape.shape)]
    for i, line in enumerate(format):
        for j, column in enumerate(list(line)):
            if column == '0':
                pygame.draw.rect(surface, shape.color,
                                 (sx + j*30, sy + i*30, 30, 30), 0)


def draw_window(surface, grid, score=0, level=1, lines=0):
    surface.fill((0, 0, 0))

    font = pygame.font.SysFont('comicsans', 60)
    label = font.render('Tetris', 1, (255, 255, 255))
    surface.blit(label, (top_left_x + play_width/2 - label.get_width()/2, 30))

    # Score
    font = pygame.font.SysFont('comicsans', 30)
    surface.blit(font.render('Score: ' + str(score), 1, (255, 255, 255)),
                 (top_left_x + play_width + 50, top_left_y + 200))
    surface.blit(font.render('Level: ' + str(level), 1, (255, 255, 255)),
                 (top_left_x + play_width + 50, top_left_y + 240))
    surface.blit(font.render('Lines: ' + str(lines), 1, (255, 255, 255)),
                 (top_left_x + play_width + 50, top_left_y + 280))

    # Campo de jogo
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            pygame.draw.rect(surface, grid[i][j],
                             (top_left_x + j*30, top_left_y + i*30, 30, 30), 0)

    pygame.draw.rect(surface, (255, 0, 0),
                     (top_left_x, top_left_y, play_width, play_height), 5)

    draw_grid(surface, grid)


# ------------------ LOOP PRINCIPAL ------------------
def main(win):
    locked_positions = {}
    grid = create_grid(locked_positions)

    change_piece = False
    run = True
    current_piece = get_shape()
    next_piece = get_shape()
    clock = pygame.time.Clock()
    fall_time = 0
    fall_speed = 0.5
    level = 1
    lines_cleared = 0
    score = 0

    # Pontuação oficial Tetris
    points = {0: 0, 1: 100, 2: 300, 3: 500, 4: 800}

    while run:
        grid = create_grid(locked_positions)
        fall_time += clock.get_rawtime()
        clock.tick()

        # queda da peça
        if fall_time/1000 >= fall_speed:
            fall_time = 0
            current_piece.y += 1
            if not valid_space(current_piece, grid) and current_piece.y > 0:
                current_piece.y -= 1
                change_piece = True

        # Eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.display.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    current_piece.x -= 1
                    if not valid_space(current_piece, grid):
                        current_piece.x += 1

                elif event.key == pygame.K_RIGHT:
                    current_piece.x += 1
                    if not valid_space(current_piece, grid):
                        current_piece.x -= 1

                elif event.key == pygame.K_DOWN:  # soft drop
                    current_piece.y += 1
                    if not valid_space(current_piece, grid):
                        current_piece.y -= 1

                elif event.key == pygame.K_UP:  # rotacionar
                    current_piece.rotation = (current_piece.rotation+1) % len(current_piece.shape)
                    if not valid_space(current_piece, grid):
                        current_piece.rotation = (current_piece.rotation-1) % len(current_piece.shape)

                elif event.key == pygame.K_SPACE:  # hard drop
                    while valid_space(current_piece, grid):
                        current_piece.y += 1
                    current_piece.y -= 1
                    change_piece = True

        shape_pos = convert_shape_format(current_piece)

        for x, y in shape_pos:
            if y > -1:
                grid[y][x] = current_piece.color

        if change_piece:
            for pos in shape_pos:
                locked_positions[(pos[0], pos[1])] = current_piece.color
            cleared = clear_rows(grid, locked_positions)
            lines_cleared += cleared
            score += points[cleared] * level

            # aumentar dificuldade a cada 10 linhas
            if lines_cleared // 10 >= level:
                level += 1
                fall_speed = max(0.12, fall_speed - 0.05)

            current_piece = next_piece
            next_piece = get_shape()
            change_piece = False

        draw_window(win, grid, score, level, lines_cleared)
        draw_next_shape(next_piece, win)
        pygame.display.update()

        if check_lost(locked_positions):
            draw_text_middle("You Lost!", 80, (255, 0, 0), win)
            pygame.display.update()
            pygame.time.delay(2000)
            run = False


def main_menu(win):
    run = True
    while run:
        win.fill((0, 0, 0))
        draw_text_middle('Press any key to play', 60, (255, 255, 255), win)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                main(win)

    pygame.quit()

win = pygame.display.set_mode((s_width, s_height))
pygame.display.set_caption('Tetris')
main_menu(win)
