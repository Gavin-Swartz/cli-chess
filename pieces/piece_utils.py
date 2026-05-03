from board import get_piece_at_square, on_board


def validate_rook_bishop_squares(player, opponent, x, y, piece):
        # Ensure no piece from same player on square
        if not get_piece_at_square(player.pieces, x, y).captured:
            return False
        # Ensure square is on board
        elif not on_board(x, y):
            return False
        # If opponent piece at square, square is valid move but discontinue search in direction
        elif not get_piece_at_square(opponent.pieces, x, y).captured:
            piece.possible_moves.append([x, y])
            return False
        # If empty square, move is valid
        else:
            piece.possible_moves.append([x, y])
            return True


def validate_free_square_for_king(opponent, x, y):
    for piece in opponent.pieces:
        # If target square is possible for opponent, it is invalid for king
        if [x, y] in piece.possible_moves:
            return False

    # Square cannot be moved to by opponent
    return True