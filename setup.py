from pieces.bishop import Bishop
from pieces.king import King
from pieces.knight import Knight
from pieces.pawn import Pawn
from pieces.queen import Queen
from pieces.rook import Rook


def generate_board(white_pieces, black_pieces):
    board = []
    for row in range(8):
        board.insert(row, ['--', '--', '--', '--', '--', '--', '--', '--'])

    # TODO: player character (w or b) in class
    for piece in white_pieces:
        board[piece.posY][piece.posX] = 'w' + piece.rep
    
    for piece in black_pieces:
        board[piece.posY][piece.posX] = 'b' + piece.rep

    return board


def instantiate_pieces():
    white_pieces = []
    black_pieces = []

    # Create pawns
    for column in range(8):
        white_pieces.append(Pawn(column, 6, 0))
        black_pieces.append(Pawn(column, 1, 1))

    # Create kings
    white_pieces.append(King(4, 7, 0))
    black_pieces.append(King(4, 0, 1))

    # Create queens
    white_pieces.append(Queen(3, 7, 0))
    black_pieces.append(Queen(3, 0, 1))

    # Create rooks
    for column in [0, 7]:
        white_pieces.append(Rook(column, 7, 0))
        black_pieces.append(Rook(column, 0, 1))

    # Create knights
    for column in [1, 6]:
        white_pieces.append(Knight(column, 7, 0))
        black_pieces.append(Knight(column, 0, 1))

    # Create bishops
    for column in [2, 5]:
        white_pieces.append(Bishop(column, 7, 0))
        black_pieces.append(Bishop(column, 0, 1))

    return white_pieces, black_pieces