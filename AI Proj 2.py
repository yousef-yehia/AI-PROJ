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



def create_board():  # create_board
    board = np.zeros((ROW_COUNT, COLUMN_COUNT))  # Define the rows and columns
    return board

def get_empty_row(board, col):   # get all empty rows at special column
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r

def is_empty(board, col): # column is empty or not
    return board[ROW_COUNT - 1][col] == 0


def empty_cols(board):  # array of empty columns
    empty_cols = []
    for col in range(COLUMN_COUNT):
        if is_empty(board, col): # call function is_empty to know if the col empty or not
            empty_cols.append(col) # add the col to array
    return empty_cols



def winning_check(board, piece):  # check if there 4 pieces horizontal or vertical or positively or negatively diaganols

    # horizontal
    for i in range(COLUMN_COUNT - 3): # if column_count = 3 => i = 0      the range [3,9]
        for j in range(ROW_COUNT):  # doesn't matter value of row because [ horizontal ]
            if board[j][i] == piece and board[j][i + 1] == piece and board[j][i + 2] == piece and \
               board[j][i + 3] == piece: # the function will ckeck if col 0,1,2 and 3 same color AI will win
               return True

    # vertical
    for i in range(COLUMN_COUNT):  # doesn't matter value of column because [ vertical ]
        for j in range(ROW_COUNT - 3):  # if row_count = 3 => j = 0  the range [3,8]
            if board[j][i] == piece and board[j + 1][i] == piece and board[j + 2][i] == piece and\
               board[j + 3][ i] == piece: # the function will ckeck if row 0,1,2 and 3 same color AI will win
               return True

    # positively diaganols
    for i in range(COLUMN_COUNT - 3): # if column_count = 3 => i = 0      the range [3,9]
        for j in range(ROW_COUNT - 3): # if row_count = 3 => j = 0  the range [3,8]
            if board[j][i] == piece and board[j + 1][i + 1] == piece and board[j + 2][i + 2] == piece and\
               board[j + 3][i + 3] == piece: # the function will ckeck if row and col [0,0],[1,1],[2,2] and [3,3] same color AI will win
               return True

    # negatively diaganols   // there is wrong syntax bcs the col should decrease and the row should increase
    for i in range(COLUMN_COUNT - 3):       # if column_count = 3 => i = 0                        the range [3,9]
        for j in range(3, ROW_COUNT):       # the row_count will start by value 3  =>  j = 3      the range [3,5]
            if board[j][i] == piece and board[j - 1][i + 1] == piece and board[j - 2][i + 2] == piece and \
               board[j - 3][i + 3] == piece: # the function will ckeck if row and col [3,0],[2,1],[1,2] and [0,3] same color AI will win
               return True



def is_terminal(board):         #  send to function winning_check to know if AI1 or AI2  win or not
    return winning_check(board, AI1_PIECE) or winning_check(board, AI2_PIECE) or len(empty_cols(board)) == 0



def evaluate_position(board, piece):
    score = 0

    def evaluate_line(line):   # calculate score
        opponent = 3 - piece   # Player 1 -> opponent 2, player 2 -> opponent 1
        num_player_pieces = np.count_nonzero(line == piece)
        num_opponent_pieces = np.count_nonzero(line == opponent)
        if num_player_pieces == 4:  # if i am player 1 and num_of_pieces = 4 the score will increase 1000
            score = 1000
        elif num_player_pieces == 3 and num_opponent_pieces == 0: #  num_of_pieces = 3 the score will increase 100
            score = 100
        elif num_player_pieces == 2 and num_opponent_pieces == 0: #  num_of_pieces = 2 the score will increase 10
            score = 10
        elif num_player_pieces == 1 and num_opponent_pieces == 0: #  num_of_pieces = 1 the score will increase 1
            score = 1
        elif num_opponent_pieces == 4: # if opponent player num_of_pieces = 4 my score will decrease 1000
            score = -1000
        elif num_opponent_pieces == 3 and num_player_pieces == 0: # num_of_pieces = 3 my score will decrease 100
            score = -100
        elif num_opponent_pieces == 2 and num_player_pieces == 0: # num_of_pieces = 2 my score will decrease 10
            score = -10
        elif num_opponent_pieces == 1 and num_player_pieces == 0: # num_of_pieces = 1 my score will decrease 1
            score = -1
        else:
            score = 0
        return score
        pass

    #Score center column
    center_count = sum(board[r][COLUMN_COUNT // 2] == piece for r in range(ROW_COUNT))
    score += center_count * 3

    # Evaluate columns
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT - 3):
            line = [board[r + i][c] for i in range(4)]
            score += evaluate_line(line)

    # Evaluate rows
    for r in range(ROW_COUNT):
        for c in range(COLUMN_COUNT - 3):
            line = board[r][c:c + 4]
            score += evaluate_line(line)

    # Evaluate positive diagonals
    for r in range(ROW_COUNT - 3):
        for c in range(COLUMN_COUNT - 3):
            line = [board[r + i][c + i] for i in range(4)]
            score += evaluate_line(line)

    # Evaluate negative diagonals
    for r in range(ROW_COUNT - 3):
        for c in range(COLUMN_COUNT - 3):
            line = [board[r + i][c + 3 - i] for i in range(4)]
            score += evaluate_line(line)

        return score



def minimaxAI1(board, depth,maximizingPlayer):
    available_cols = empty_cols(board)
    terminal = is_terminal(board)
    if depth == 0 or terminal:
        if terminal:
            if winning_check(board, AI1_PIECE):
                return (None, 999999999999999)
            elif winning_check(board, AI2_PIECE):
                return (None, -999999999999999)
            else:                           # Game is over, no more valid moves
                return (None, 0)
        else:                               # Depth is zero
            return (None, evaluate_position(board, AI1_PIECE))
    if maximizingPlayer:       # maximizing player
        value = -math.inf
        column = 0
        for col in available_cols:
            row = get_empty_row(board, col)
            b_copy = board.copy()
            b_copy[row][col] = AI1_PIECE
            new_score = minimaxAI1(b_copy, depth - 1, False)[1]
            if new_score > value:
                value = new_score
                column = col
        return column, value

    else:                        # Minimizing player
        value = math.inf
        column = 0
        for col in available_cols:
            row = get_empty_row(board, col)
            b_copy = board.copy()
            b_copy[row][col] = AI2_PIECE
            new_score = minimaxAI1(b_copy, depth - 1, True)[1]
            if new_score < value:
                value = new_score
                column = col
        return column, value


def minimaxAI2(board, depth,maximizingPlayer):
    available_cols = empty_cols(board)
    terminal = is_terminal(board)
    if depth == 0 or terminal:
        if terminal:
            if winning_check(board, AI2_PIECE):
                return (None, 999999999999999)
            elif winning_check(board, AI1_PIECE):
                return (None, -999999999999999)
            else:                     # Game is over, no more valid moves
                return (None, 0)
        else:                         # Depth is zero
            return (None, evaluate_position(board, AI2_PIECE))
    if maximizingPlayer:             # maximizing player
        value = -math.inf
        column = 0
        for col in available_cols:
            row = get_empty_row(board, col)
            b_copy = board.copy()
            b_copy[row][col] = AI2_PIECE
            new_score = minimaxAI2(b_copy, depth - 1, False)[1]
            if new_score > value:
                value = new_score
                column = col
        return column, value

    else:                         # Minimizing player
        value = math.inf
        column = 0
        for col in available_cols:
            row = get_empty_row(board, col)
            b_copy = board.copy()
            b_copy[row][col] = AI1_PIECE
            new_score = minimaxAI2(b_copy, depth - 1, True)[1]
            if new_score < value:
                value = new_score
                column = col
        return column, value



def alphaBetaAI1(board, depth, alpha, beta, maximizingPlayer):
    available_cols = empty_cols(board)
    terminal = is_terminal(board)
    if depth == 0 or terminal:
        if terminal:
            if winning_check(board, AI1_PIECE):
                return (None, 999999999999999)
            elif winning_check(board, AI2_PIECE):
                return (None, -999999999999999)
            else:                          # Game is over, no more valid moves
                return (None, 0)
        else:                              # Depth is zero
            return (None, evaluate_position(board, AI1_PIECE))
    if maximizingPlayer:               # maximizing player
        value = -math.inf
        column = 0
        for col in available_cols:
            row = get_empty_row(board, col)
            b_copy = board.copy()
            b_copy[row][col] = AI1_PIECE
            new_score = alphaBetaAI1(b_copy, depth - 1, alpha, beta, False)[1]
            if new_score > value:
                value = new_score
                column = col
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return column, value

    else:                          # Minimizing player
        value = math.inf
        column = 0
        for col in available_cols:
            row = get_empty_row(board, col)
            b_copy = board.copy()
            b_copy[row][col] = AI2_PIECE
            new_score = alphaBetaAI1(b_copy, depth - 1, alpha, beta, True)[1]
            if new_score < value:
                value = new_score
                column = col
            beta = min(beta, value)
            if alpha >= beta:
                break
        return column, value


def alphaBetaAI2(board, depth, alpha, beta, maximizingPlayer):
    available_cols = empty_cols(board)
    terminal = is_terminal(board)
    if depth == 0 or terminal:
        if terminal:
            if winning_check(board, AI2_PIECE):
                return (None, 999999999999999)
            elif winning_check(board, AI1_PIECE):
                return (None, -999999999999999)
            else:                        # Game is over, no more valid moves
                return (None, 0)
        else:                            # Depth is zero
            return (None, evaluate_position(board, AI2_PIECE))
    if maximizingPlayer:                 # maximizing player
        value = -math.inf
        column = 0
        for col in available_cols:
            row = get_empty_row(board, col)
            b_copy = board.copy()
            b_copy[row][col] = AI2_PIECE
            new_score = alphaBetaAI2(b_copy, depth - 1, alpha, beta, False)[1]
            if new_score > value:
                value = new_score
                column = col
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return column, value

    else:                           # Minimizing player
        value = math.inf
        column = 0
        for col in available_cols:
            row = get_empty_row(board, col)
            b_copy = board.copy()
            b_copy[row][col] = AI1_PIECE
            new_score = alphaBetaAI2(b_copy, depth - 1, alpha, beta, True)[1]
            if new_score < value:
                value = new_score
                column = col
            beta = min(beta, value)
            if alpha >= beta:
                break
        return column, value

