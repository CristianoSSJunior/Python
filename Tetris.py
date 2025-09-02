# Jogo Tetris, criado 20/08/2025
# Update: 25/08/2025

import pygame
import random

pygame.font.init()
 
# creating the data structure for pieces
# setting up global vars
# functions
# - create_grid
# - draw_grid
# - draw_window
# - rotating shape in main
# - setting up the main
 
"""
10 x 20 square grid
shapes: S, Z, I, O, J, L, T
represented in order by 0 - 6
"""
 
# GLOBALS VARS
s_width = 800
s_height = 700
play_width = 300  # meaning 300 // 10 = 30 width per block
play_height = 600  # meaning 600 // 20 = 20 height per block
block_size = 30
 
top_left_x = (s_width - play_width) // 2
top_left_y = s_height - play_height
 
 
# SHAPE FORMATS
S = [['.....', '.....', '..00..', '.00...', '.....'],
['.....', '..0..', '..00.', '...0.', '.....']]

Z = [['.....', '.....', '.00..', '..00.', '.....'],
['.....', '..0..', '.00..', '.0...', '.....']]

I = [['..0..', '..0..', '..0..', '..0..', '.....'],
['.....', '0000.', '.....', '.....', '.....']]

O = [['.....', '.....', '.00..', '.00..', '.....']]

J = [['.....', '.0...', '.000.', '.....', '.....'],
['.....', '..00.', '..0..', '..0..', '.....'],
['.....', '.....', '.000.', '...0.', '.....'],
['.....', '..0..', '..0..', '.00..', '.....']]

L = [['.....', '...0.', '.000.', '.....', '.....'],
['.....', '..0..', '..0..', '..00.', '.....'],
['.....', '.....', '.000.', '.0...', '.....'],
['.....', '.00..', '..0..', '..0..', '.....']]

T = [['.....', '..0..', '.000.', '.....', '.....'],
['.....', '..0..', '..00.', '..0..', '.....'],
['.....', '.....', '.000.', '..0..', '.....'],
['.....', '..0..', '.00..', '..0..', '.....']]
 
shapes = [S, Z, I, O, J, L, T]
shape_colors = [(0, 255, 0), (255, 0, 0), (0, 255, 255), (255, 255, 0), (255, 165, 0), (0, 0, 255), (128, 0, 128)]
# index 0 - 6 represent shape
# i = index of shape
# j = index of rotation
# x = column
# y = row
# pos = (x, y)
 
# -- Class -- 
class Piece(object):
    def __init__(self, x, y, shape):
        self.x = x
        self.y = y
        self.shape = shape
        self.color = shape_colors[shapes.index(shape)]
        self.rotation = 0

# -- Functions --
def create_grid(locked_positions={}):
    grid = [[(0, 0, 0) for _ in range(10)] for _ in range(20)]
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if (x, y) in locked_positions:
                color = locked_positions[(x, y)]
                grid[y][x] = color
    return grid
 
def convert_shape_format(shape):
    positions = []
    format = shape.shape[shape.rotation % len(shape.shape)]

    for i, line in enumerate(format):
        row = list(line)
        for j, column in enumerate(row):
            if column == '0':
                positions.append((shape.x + j - 2, shape.y + i - 4))
    return positions
 
def valid_space(shape, grid):
    accepted_positions = [[(x, y) for x in range(10) if grid[y][x] == (0,0,0)] for y in range(20)]
    accepted_positions = [x for sublist in accepted_positions for x in sublist]

    formatted_shape = convert_shape_format(shape)

    for pos in formatted_shape:
        x, y = pos  
        if x < 0 or x >= 10 or y >= 20:
            return False
        if y >= 0 and (x, y) not in accepted_positions:
            return False
    return True

def check_lost(locked_positions):
    for pos in locked_positions:
        x, y = pos
        if y < 1:  # if any piece is above the top of the grid
            return True
    return False 
 
def get_shape():
    shape = random.choice(shapes)
    return Piece(5, 0, shape)
 
def draw_text_middle(text, size, color, surface):
    font = pygame.font.SysFont('comicsans', size, bold=True)
    label = font.render(text, 1, color)
    surface.blit(label, (top_left_x + play_width/2 - (label.get_width()/2), 
                         top_left_y + play_height/2 - label.get_height()/2))
   
def draw_grid(surface, grid):
    sx = top_left_x
    sy = top_left_y

    for i in range(len(grid)):
        pygame.draw.line(surface, (128,128,128), (sx, sy + i*30), (sx + play_width, sy + i * 30))  # horizontal lines
        for j in range(len(grid[i])):
            pygame.draw.line(surface, (128,128,128), (sx + j*30, sy), (sx + j * 30, sy + play_height))

def clear_rows(grid, locked):
    # Need to check if row is clear then shift every other row above down one
    inc = 0
    ind = -1
    for i in range(len(grid)-1, -1, -1):
        row = grid[i]
        if (0,0,0) not in row:
            inc += 1
            ind = i
            for j in range(len(row)):
                try:
                    del locked[(j, i)]
                except:
                    continue
    if inc > 0:
        # shift every row above down
        for key in sorted(list(locked), key=lambda x: x[1])[::-1]:
            x, y = key
            if y < ind:
                newKey = (x, y + inc)
                locked[newKey] = locked.pop(key)
    return inc

def draw_next_shape(shape, surface):
    font = pygame.font.SysFont('comicsans', 30)
    label = font.render('Next Shape', 1, (255,255,255))

    sx = top_left_x + play_width + 50
    sy = top_left_y + (play_height / 2 - 100)
    format = shape.shape[shape.rotation % len(shape.shape)]
    for i, line in enumerate(format):
        row = list(line)
        for j, column in enumerate(row):
            if column == '0':
                pygame.draw.rect(surface, shape.color, (sx + j*30, sy + i*30, 30, 30), 0)
    
    surface.blit(label, (sx + 10, sy - 30))

def draw_hold_shape(shape, surface):
    font = pygame.font.SysFont('comicsans', 30)
    label = font.render('Hold', 1, (255,255,255))

    sx = top_left_x - 200 
    sy = top_left_y + 100
    surface.blit(label, (sx + 20, sy - 30))
    if shape:
        format = shape.shape[shape.rotation % len(shape.shape)]
        for i, line in enumerate(format):
            row = list(line)
            for j, column in enumerate(row):
                if column == '0':
                    pygame.draw.rect(surface, shape.color, (sx + j*30, sy + i*30, 30, 30), 0)
    

def draw_window(surface, grid, score=0, lines=0, level=1):
    surface.fill((0,0,0))

    # Tetris Title
    font = pygame.font.SysFont('comicsans', 60)
    label = font.render('Tetris', 1, (255, 255, 255))
    surface.blit(label, (top_left_x + play_width / 2 - label.get_width()/2, 30))
    
    # Score, Lines and Level
    font = pygame.font.SysFont('comicsans', 30)
    surface.blit(font.render('Score: ' + str(score), 1, (255,255,255)),
        (top_left_x - 200, top_left_y + 200))
    surface.blit(font.render('Lines: ' + str(lines), 1, (255, 255, 255)),
        (top_left_x - 200, top_left_y + 250))
    surface.blit(font.render('Level: ' + str(level), 1, (255, 255, 255)),
        (top_left_x - 200, top_left_y + 300))


    sx = top_left_x + play_width + 50
    sy = top_left_y + (play_height / 2 - 100)

    #Game grid
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            pygame.draw.rect(surface, grid[i][j],
                (top_left_x + j * 30, top_left_y + i * 30, 30, 30), 0)
            
    pygame.draw.rect(surface, (255, 0, 0),
                (top_left_x, top_left_y, play_width, play_height), 5)
    
    draw_grid(surface, grid)

def draw_ghost(piece, grid, surface):
    ghost = Piece(piece.x, piece.y, piece.shape)
    ghost.rotation = piece.rotation
    while valid_space(ghost, grid):
        ghost.y += 1
    ghost.y -= 1  # Move back to last valid position

    ghost_pos = convert_shape_format(ghost)
    
    r,g,b = piece.color
    ghost_surface = pygame.Surface((30,30), pygame.SRCALPHA)  # Create a surface with alpha channel
    ghost_surface.fill((r, g, b, 80))  # Fill with color

    for pos in ghost_pos:
        x, y = pos
        if y > -1:
            surface.blit(ghost_surface, (top_left_x + x * 30, top_left_y + y * 30))

def hold_piece(current, hold, can_hold):
    if not can_hold:
        return current, hold, False

    if hold is None:
        hold = current
        current = get_shape()
    else:
        current, hold = hold, current
        hold.x, hold.y = 5, 0  # Reset position of held piece
    return current, hold, False
    
# --- Main Game Loop ---
def main(win):
    locked_positions = {}
    grid = create_grid(locked_positions)

    # Delay Lock
    lock_delay = 500  # milliseconds
    lock_start = None

    change_piece = False
    run = True
    current_piece = get_shape()
    next_piece = get_shape()
    hold_piece_var = None
    can_hold = True
    clock = pygame.time.Clock()
    fall_time = 0
    fall_speed = 0.27
    level = 1

    # scoring system
    lines_cleared = 0
    score = 0
    # Points system, from Official Tetris
    points = {0:0, 1:100, 2:300, 3:500, 4:800}

    while run:
        grid = create_grid(locked_positions)
        fall_time += clock.get_rawtime()
        clock.tick()

        # --- PIECE FALLING LOGIC ---
        if fall_time / 1000 >= fall_speed:
            fall_time = 0
            current_piece.y += 1
            if not (valid_space(current_piece, grid)) and current_piece.y > 0:
                current_piece.y -= 1
                # Lock delay
                if lock_start is None:
                    lock_start = pygame.time.get_ticks()
                elif pygame.time.get_ticks() - lock_start >= lock_delay:
                    change_piece = True
            else:
                lock_start = None
                
        # ---- User input ----
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.display.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    current_piece.x -= 1
                    if not valid_space(current_piece, grid):
                        current_piece.x += 1
                    else:
                        lock_start = None
                    
                elif event.key == pygame.K_RIGHT:
                    current_piece.x += 1
                    if not valid_space(current_piece, grid):
                        current_piece.x -= 1
                    else:
                        score += 1
                        lock_start = None

                # Soft drop
                elif event.key == pygame.K_DOWN:
                    current_piece.y += 1
                    if not valid_space(current_piece, grid):
                        current_piece.y -= 1
                    else:
                        score += 1
                        lock_start = None

                # Rotate shape
                elif event.key == pygame.K_UP:
                    current_piece.rotation = (current_piece.rotation + 1) % len(current_piece.shape)
                    if not valid_space(current_piece, grid):
                        current_piece.rotation = (current_piece.rotation -1) % len(current_piece.shape)
                    else:
                        lock_start = None

                # Hard drop
                elif event.key == pygame.K_SPACE:
                    while valid_space(current_piece, grid):
                        current_piece.y += 1
                        score += 2
                    current_piece.y -= 1
                    change_piece = True

                # Hold piece
                elif event.key == pygame.K_c:
                    current_piece, hold_piece_var, can_hold = hold_piece(current_piece, hold_piece_var, can_hold)

        # ---- Drawing the window ----
        draw_window(win, grid, score, lines_cleared, level)
        draw_next_shape(next_piece, win)
        draw_hold_shape(hold_piece_var, win)
        draw_ghost(current_piece, grid, win)

        shape_pos = convert_shape_format(current_piece)
        for x, y in shape_pos:
            if y > -1:
                pygame.draw.rect(win, current_piece.color,
                         (top_left_x + x*30, top_left_y + y*30, 30, 30), 0)

        pygame.display.update()

        if change_piece:
            for pos in shape_pos:
                p = (pos[0], pos[1])
                locked_positions[p] = current_piece.color
            cleared = clear_rows(grid, locked_positions)
            lines_cleared += cleared
            score += points[cleared] * level

            # higher difficulty for every 10 lines cleared
            if lines_cleared // 10 >= level:
                level += 1
                fall_speed = max(0.12, fall_speed - 0.05)
            
            current_piece = next_piece
            next_piece = get_shape()
            change_piece = False
            lock_start = None

        # Check if user lost
        if check_lost(locked_positions):
            draw_text_middle('You Lost!', 80, (255, 0, 0), win)
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

# --- Start Game ---
win = pygame.display.set_mode((s_width, s_height))
pygame.display.set_caption('Tetris')
main_menu(win)  # start game