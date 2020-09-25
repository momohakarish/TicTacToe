import pygame


# Draws a tic tac toe board to the screen
def draw_board(screen, color, screen_width, screen_height, block_size, line_width):
    for x in range((screen_width // block_size) - 1):
        pygame.draw.line(screen, color, ((x+1) * block_size, 0), ((x+1) * block_size, screen_height), line_width)
    for y in range((screen_height // block_size) - 1):
        pygame.draw.line(screen, color, (0, (y+1) * block_size), (screen_height, (y+1) * block_size), line_width)


# Draws an image to the screen
def draw_image(screen, path, coordinates):
    img = pygame.image.load(path)
    screen.blit(img, coordinates)


def get_transparent_surface(width, height, transparent_alpha, color):
    temp = pygame.Surface((width, height))
    temp.set_alpha(transparent_alpha)
    temp.fill(color)
    return temp


def create_text(text, font, size, color):
    # Creating our game over text
    text_font = pygame.font.SysFont(font, size)
    return text_font.render(text, True, color)
