from setup import generate_board, instantiate_pieces


def main():
    # Instantiate pieces
    white_pieces, black_pieces = instantiate_pieces()

    # Generate chess board
    board = generate_board(white_pieces, black_pieces)

    # Print board
    for row in board:
        print(row)


if __name__ == "__main__":
    main()