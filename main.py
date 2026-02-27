from board import display_board, generate_board
from pieces.piece import Piece
from player import Player
from setup import instantiate_pieces, instantiate_players

# TODO: move or update logic for converting chars to ints
col_letters = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}

def process_command(command, player: Player) -> bool:
    # Command structure:
    # Ex: E2 E4
    # (from) (to)

    # Parse command and check command validity
    parsed_command = command.split(' ')

    # Command should have exactly 2 arguments
    if len(parsed_command) != 2:
        print('Invalid command entered. Try again.')
        return False
    for arg in parsed_command:
        # Each argument in command should have 2 characters: the first alphabetical and the second a numeric digit
        if (len(arg) != 2) or not (arg[0].isalpha()) or not (arg[1].isdigit()):
            print('Invalid command entered. Try again.')
            return False
    start, dst = parsed_command

    # Get starting index
    start_col = col_letters[start[0].upper()]   # Get letter (column)
    start_row = 8 - int(start[1])               # Get number (row)

    # Get piece at location
    selected_piece = Piece(-1, -1, True)    # Will always be invalid, used as placeholder
    for piece in player.pieces:
        if (piece.posX == start_col) and (piece.posY == start_row) and not piece.captured:
            selected_piece = piece
            print(f'Piece found: {piece.rep}')

    if selected_piece.captured:
        print('Invalid piece selected. Try again.')
        return False
    else:
        # TODO: check valid (on board, within piece limitations, no existing piece from same player)
        # Get destination index
        dst_col = col_letters[dst[0]]
        dst_row = 8 - int(dst[1])

        # Move piece
        selected_piece.move(dst_col, dst_row)
        return True


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
            valid_command = False
            while not valid_command:
                command = input(f"({player.color}) Enter Move: ")
                valid_command = process_command(command, player)
            
            # Update board
            board = generate_board(white, black)


if __name__ == "__main__":
    main()