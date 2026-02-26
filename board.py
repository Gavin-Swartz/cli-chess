from player import Player


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
