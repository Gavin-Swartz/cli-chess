from board import display_board, generate_board
from setup import instantiate_pieces, instantiate_players


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

            # TODO: Process user input
            
            player.pieces[0].move(0, 4)     # Testing piece movement

            # Update board
            board = generate_board(white, black)


if __name__ == "__main__":
    main()