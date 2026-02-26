from setup import generate_board, instantiate_pieces, instantiate_players


def main():
    # Instantiate players
    white, black = instantiate_players()

    # Instantiate pieces
    instantiate_pieces(white, black)

    # Generate chess board
    board = generate_board(white, black)

    # Print board
    for row in board:
        print(row)


if __name__ == "__main__":
    main()