from pieces.bishop import Bishop
from pieces.king import King
from pieces.knight import Knight
from pieces.pawn import Pawn
from pieces.queen import Queen
from pieces.rook import Rook
from player import Player


def generate_board(white, black):
    board = []
    for row in range(8):
        board.insert(row, ['--', '--', '--', '--', '--', '--', '--', '--'])

    # TODO: player character (w or b) in class
    for piece in white.pieces:
        board[piece.posY][piece.posX] = 'w' + piece.rep
    
    for piece in black.pieces:
        board[piece.posY][piece.posX] = 'b' + piece.rep

    return board


def instantiate_pieces(white: Player, black: Player):
    # Create pawns
    for column in range(8):
        white.pieces.append(Pawn(column, 6, 0))
        black.pieces.append(Pawn(column, 1, 1))

    # Create kings
    white.pieces.append(King(4, 7, 0))
    black.pieces.append(King(4, 0, 1))

    # Create queens
    white.pieces.append(Queen(3, 7, 0))
    black.pieces.append(Queen(3, 0, 1))

    # Create rooks
    for column in [0, 7]:
        white.pieces.append(Rook(column, 7, 0))
        black.pieces.append(Rook(column, 0, 1))

    # Create knights
    for column in [1, 6]:
        white.pieces.append(Knight(column, 7, 0))
        black.pieces.append(Knight(column, 0, 1))

    # Create bishops
    for column in [2, 5]:
        white.pieces.append(Bishop(column, 7, 0))
        black.pieces.append(Bishop(column, 0, 1))


def instantiate_players():
    white = Player('w', 0)
    black = Player('b', 1)

    return white, black