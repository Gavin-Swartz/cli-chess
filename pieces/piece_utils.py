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