

from pieces.pawn import Pawn


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
        black_pieces.append(Pawn(column, 1, 0))

    return white_pieces, black_pieces