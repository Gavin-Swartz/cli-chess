from turn_utils import get_position_from_algebraic_notation, validate_command, set_previously_moved_piece
from player import Player
from pieces.pawn import Pawn
from setup import instantiate_pieces, instantiate_players
from board import display_board, generate_board, get_piece_at_square
    

def handle_turn(player: Player, opponent: Player) -> bool:
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

    # Get piece at origin square
    selected_piece = get_piece_at_square(player.pieces, origin_col, origin_row)
    if selected_piece.captured:
        print('No valid piece at square. Try again.')
        return False

    # Ensure move is valid for piece type and move
    if [target_col, target_row] in selected_piece.possible_moves:
        selected_piece.move(target_col, target_row)
        set_previously_moved_piece(selected_piece)

        # Capture opponent's piece (if at target)
        target_piece = get_piece_at_square(opponent.pieces, target_col, target_row)
        if not target_piece.captured:
            target_piece.captured = True
            print(f"Captured opponent's {target_piece.name}")

        # Check if pawn reached furthest rank from starting position and allow promotion
        if (type(selected_piece) is Pawn) and selected_piece.y in [0, 7]:
            selected_piece.promote_pawn(player)

        return True
    else:
        print('Invalid move. Try again.')
        return False


def main():
    # Instantiate players and pieces
    white, black = instantiate_players()
    players = [white, black]
    instantiate_pieces(white, black)

    # Generate chess board
    board = generate_board(white, black)

    # Game loop
    game_state = True
    while game_state:
        for player in players:
            # Print board at beginning of every player's turn
            display_board(board)

            # Get opponent of the player whose turn it currently is
            opponent_index = (players.index(player) + 1) % 2
            opponent = players[opponent_index]

            # Get all validate movements for all pieces
            for piece in player.pieces:
                piece.update_valid_moves(player, opponent)

                # Printing possible moves for each piece for testing
                if piece.captured:
                    print(piece.name, '[CAPTURED]')
                else:
                    print(piece.name, piece.possible_moves)

            # Get user input
            valid_command = False
            while not valid_command:
                valid_command = handle_turn(player, opponent)
            
            # Update board
            board = generate_board(white, black)


if __name__ == "__main__":
    main()