from turn_utils import get_position_from_algebraic_notation, validate_command
from player import Player
from pieces.piece import Piece
from setup import instantiate_pieces, instantiate_players
from board import display_board, generate_board, on_board
    

def handle_turn(player: Player) -> bool:
    # Get user input and parse
    command = input(f"({player.color}) Enter Move: ")
    parsed_command = command.split(' ')

    # Check input validity
    if not validate_command(parsed_command):
        print('Invalid command entered. Try again.')
        return False
    
    # Parse input into origin and target squares and get list indices
    origin, target = parsed_command
    origin_col, origin_row = get_position_from_algebraic_notation(origin)
    target_col, target_row = get_position_from_algebraic_notation(target)

    # Verify target square is valid
    if not on_board(target_col, target_row):
        print('Target square is invalid. Try again.')
        return False
    
    # Get piece at target square
    selected_piece = Piece(-1, -1, True)    # Will always be invalid, used as placeholder
    for piece in player.pieces:
        if (piece.posX == origin_col) and (piece.posY == origin_row) and not piece.captured:
            selected_piece = piece
            print(f'Piece found: {piece.rep}')

    if selected_piece.captured:
        print('No valid piece at square. Try again.')
        return False
    else:
        selected_piece.move(target_col, target_row)
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
                valid_command = handle_turn(player)
            
            # Update board
            board = generate_board(white, black)


if __name__ == "__main__":
    main()