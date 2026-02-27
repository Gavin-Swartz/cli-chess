from typing import List

from pieces.piece import Piece
from player import Player

# Map column letters to index value
col_letters = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}

def generate_board(white: Player, black: Player):
    # Create empty board
    board = []
    for row in range(8):
        board.insert(row, ['--', '--', '--', '--', '--', '--', '--', '--'])

    # Fill board with pieces
    for player in [white, black]:
        for piece in player.pieces:
            board[piece.posY][piece.posX] = player.color + piece.rep

    return board


def display_board(board):
    for row in board:
        print(row)


def on_board(x: int, y: int) -> bool:
    upper = 7
    lower = 0

    if x in range(lower, upper) and y in range(lower, upper):
        return True
    else:
        return False
    

def get_col_letters():
    return col_letters


def get_piece_at_square(pieces: List[Piece], x: int, y: int) -> Piece:
    selected_piece = Piece(-1, -1, True)    # Will always be invalid, used as placeholder
    for piece in pieces:
        if (piece.posX == x) and (piece.posY == y) and not piece.captured:
            selected_piece = piece

    return selected_piece


def get_column_index_from_alpha_char(letter) -> int:
    letter = letter.upper()
    return col_letters[letter]
