import pygame
import os
import DrawingFunctions
from Board import Board
from Timer import Timer

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 900
GAME_WIDTH = 900
GAME_HEIGHT = 900
DIMENSIONS = (SCREEN_WIDTH, SCREEN_HEIGHT)

WINDOW_STARTING_X_POS = 480
WINDOW_STARTING_Y_POS = 50

X_SIGN = 'x'
O_SIGN = 'o'
MAX_NUMBER_OF_TURNS = 9

DEFAULT_TEXT_FONT = 'arial'
DEFAULT_TEXT_SIZE = 96

BLOCK_SIZE = 300
FPS = 144
TRANSPARENT_ALPHA = 128

BLACK = (0, 0, 0)
WHITE = (250, 250, 250)

LEFT_CLICK = 1


def on_left_click(pos):
    global x_turn, count
    x = pos[0] // BLOCK_SIZE
    y = pos[1] // BLOCK_SIZE

    if board.get_cell(x, y) != board.EMPTY_CELL:    # If cell already clicked on do nothing
        return

    count += 1      # Incrementing the turn counter

    if x_turn:
        board.set_cell(x, y, X_SIGN)
        DrawingFunctions.draw_image(screen, 'media/cross.png', (x * BLOCK_SIZE, y * BLOCK_SIZE))
    else:
        board.set_cell(x, y, O_SIGN)
        DrawingFunctions.draw_image(screen, 'media/circle.png', (x * BLOCK_SIZE, y * BLOCK_SIZE))


def create_text(text, font, size, color):
    # Creating our game over text
    text_font = pygame.font.SysFont(font, size)
    return text_font.render(text, True, color)


def display_draw():
    draw_surface = DrawingFunctions.get_transparent_surface(GAME_WIDTH, GAME_HEIGHT, TRANSPARENT_ALPHA, WHITE)
    text = create_text('Draw', DEFAULT_TEXT_FONT, DEFAULT_TEXT_SIZE, BLACK)

    draw_surface.blit(text, (GAME_WIDTH // 2 - text.get_width() // 2, GAME_HEIGHT // 2 - text.get_height() // 2))
    screen.blit(draw_surface, (0, 0))


def display_win():
    win_surface = DrawingFunctions.get_transparent_surface(GAME_WIDTH, GAME_HEIGHT, TRANSPARENT_ALPHA, WHITE)

    if x_turn:
        won_sign = X_SIGN
    else:
        won_sign = O_SIGN
    text = create_text(f'Player {won_sign.upper()} Won!', DEFAULT_TEXT_FONT, DEFAULT_TEXT_SIZE, BLACK)

    win_surface.blit(text, (GAME_WIDTH // 2 - text.get_width() // 2, GAME_HEIGHT // 2 - text.get_height() // 2))
    screen.blit(win_surface, (0, 0))


def main():
    # Resetting the global game variables
    global running, x_turn, game_over, count
    running = True
    x_turn = True
    game_over = False
    count = 0

    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if game_over:
                continue
            if count == MAX_NUMBER_OF_TURNS:
                game_over = True
                display_draw()
            if event.type == pygame.MOUSEBUTTONDOWN:  # On mouse click
                position = pygame.mouse.get_pos()
                if event.button == LEFT_CLICK:
                    on_left_click(position)
                if board.player_won():
                    if x_turn:
                        display_win()
                    else:
                        display_win()
                    game_over = True
                x_turn = not x_turn  # Changing the turn

        pygame.display.update()


# Initializing the game
os.environ['SDL_VIDEO_WINDOW_POS'] = f'{WINDOW_STARTING_X_POS},{WINDOW_STARTING_Y_POS}'  # Setting the initial starting position of the window in the middle of the screen
pygame.init()

# Creating the game and setting it up
screen = pygame.display.set_mode(DIMENSIONS)
pygame.display.set_caption('Tic Tac Toe')
clock = pygame.time.Clock()     # FPS clock

# Displaying icon
icon_surface = pygame.image.load('media/icon.ico')
pygame.display.set_icon(icon_surface)


# Drawing and creating the board
board = Board()
DrawingFunctions.draw_board(screen, WHITE, SCREEN_WIDTH, SCREEN_HEIGHT, BLOCK_SIZE, 3)

# Creating our timer
timer = Timer(screen)

# Setting up the global game variables and loop
running = True
x_turn = True
game_over = False
count = 0

main()
#
# while running:
#     clock.tick(FPS)
#
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         if game_over:
#             continue
#         if count == MAX_NUMBER_OF_TURNS:
#             game_over = True
#             display_draw()
#         if event.type == pygame.MOUSEBUTTONDOWN: # On mouse click
#             position = pygame.mouse.get_pos()
#             if event.button == LEFT_CLICK:
#                 on_left_click(position)
#             if board.player_won():
#                 if x_turn:
#                     display_win()
#                 else:
#                     display_win()
#                 game_over = True
#             x_turn = not x_turn     # Changing the turn
#
#     pygame.display.update()


