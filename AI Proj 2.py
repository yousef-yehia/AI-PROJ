import numpy as np
import random
import pygame
import sys
import math

# colors of game
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
ORANGE = (255,140,0)
WHITE = (255, 255, 255)


# size
SQUARE_SIZE = 100
ROW_COUNT = 6
COLUMN_COUNT = 7
SCREEN_WIDTH = COLUMN_COUNT * SQUARE_SIZE      # 7 * 100 = 700
SCREEN_HEIGHT = (ROW_COUNT + 1) * SQUARE_SIZE  # 7 * 100 = 700
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("CONNECT-4")        # title


# Define AI 1 and AI 2
AI1 = 0
AI2 = 1


# Define the AI pieces
AI1_PIECE = 1
AI2_PIECE = 2
EMPTY = 0


# Define the  difficulty
difficulty = 0


pygame.init()       # Start game


#Fonts
FONT_SIZE = 40
font = pygame.font.SysFont("Times New Roman", 40)  # font size of words
header_font = pygame.font.SysFont("Times New Roman", 65)  # font size of Header [ choose Algorithm , choose Level ]


# GUI of Choose Algorithm
ch = "Choose Algorithm"
options = {"Minimax Alpha-Beta": 1, "Minimax": 2}
selected_option = None

while not selected_option:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            for option, value in options.items():
                x = SCREEN_WIDTH / 3.5 + list(options.keys()).index(option) * (SCREEN_WIDTH / 2)
                y = SCREEN_HEIGHT / 2
                if (
                        x - FONT_SIZE < mouse_pos[0] < x + FONT_SIZE
                        and y - FONT_SIZE < mouse_pos[1] < y + FONT_SIZE
                ):
                    selected_option = option

    screen.fill(BLACK)
    # print Choose Algorithm above the options
    ch_text = header_font.render(ch, True, WHITE)
    ch_rect = ch_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4))
    screen.blit(ch_text, ch_rect)

    # print the options of Algorithm
    for i, option in enumerate(options.keys()):
        x = SCREEN_WIDTH / 3.5 + i * (SCREEN_WIDTH / 2)
        y = SCREEN_HEIGHT / 2
        text = font.render(option, True, YELLOW)
        rect = text.get_rect(center=(x, y))
        screen.blit(text, rect)

    pygame.display.update()

pygame.time.wait(1000)  # wait 1s to go to Choose Level
algorithm = options[selected_option] if selected_option else None
print(algorithm)



# GUI of Choose Level
ch_difficulty = "Choose Level"
difficulty_levels = {"hard": 5, "medium": 3, "easy": 1}
selected_difficulty = None

while not selected_difficulty:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            for difficulty, value in difficulty_levels.items():
                x = SCREEN_WIDTH / 4 + list(difficulty_levels.keys()).index(difficulty) * (SCREEN_WIDTH / 4)
                y = SCREEN_HEIGHT / 2
                if x - FONT_SIZE < mouse_pos[0] < x + FONT_SIZE and y - FONT_SIZE < mouse_pos[1] < y + FONT_SIZE:
                    selected_difficulty = difficulty

    screen.fill(BLACK)
    # print Choose Level above difficulty_levels
    ch_text = header_font.render(ch_difficulty, True, WHITE)
    ch_rect = ch_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4))
    screen.blit(ch_text, ch_rect)

    # print difficulty_levels
    for i, difficulty in enumerate(difficulty_levels.keys()):
        x = SCREEN_WIDTH / 4 + i * (SCREEN_WIDTH / 4)
        y = SCREEN_HEIGHT / 2
        text = font.render(difficulty, True, YELLOW)
        rect = text.get_rect(center=(x, y))
        screen.blit(text, rect)

    pygame.display.update()

pygame.time.wait(1000) # wait 1s to go to start the game
difficulty = difficulty_levels[selected_difficulty]
print(difficulty)
