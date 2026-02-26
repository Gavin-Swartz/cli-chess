from board import display_board, generate_board
from pieces.piece import Piece
from player import Player
from setup import instantiate_pieces, instantiate_players

# TODO: move or update logic for converting chars to ints
col_letters = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}

def process_command(command, player: Player):
    # Command structure:
    # Ex: E2 E4
    # (from) (to)
    # TODO: check valid command structure

    # Parse command
    start, dst = command.split(' ')

    # Get starting index
    start_col = col_letters[start[0]]
    start_row = 8 - int(start[1])

    # Get piece at location
    selected_piece = Piece(-1, -1, True)    # Will always be invalid, used as placeholder
    for piece in player.pieces:
        if (piece.posX == start_col) and (piece.posY == start_row) and not piece.captured:
            selected_piece = piece
            print(f'Piece found: {piece.rep}')

    if selected_piece.captured:
        # TODO: allow player to try again
        print('Invalid piece selected! Try again!')
    else:

        # Get destination index
        # TODO: check valid (on board, within piece limitations, no existing piece from same player)
        dst_col = col_letters[dst[0]]
        dst_row = 8 - int(dst[1])

        # Move piece
        selected_piece.move(dst_col, dst_row)


def main():
    # Instantiate players and pieces
    white, black = instantiate_players()
    instantiate_pieces(white, black)

    # Generate chess board
    board = generate_board(white, black)

    # Game loop
    game_state = True
    while game_state:
        for player in [white, black]:
            # Print board
            display_board(board)

            # Get user input
            command = input(f"({player.color}) Enter Move: ")
            process_command(command, player)
            
            # Update board
            board = generate_board(white, black)


if __name__ == "__main__":
    main()