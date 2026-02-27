from typing import List
from board import get_col_letters, get_column_index_from_alpha_char


def validate_command(parsed_command: List[str]) -> bool:
    # Command should have exactly 2 arguments
    if len(parsed_command) != 2:
        return False
    for arg in parsed_command:
        # Each argument in command should have 2 characters: the first a letter between A and H and the second a numeric digit
        if (len(arg) != 2) or not (arg[0] in get_col_letters()) or not (arg[1].isdigit()):
            return False
    return True


def get_position_from_algebraic_notation(square_alg: str):
    col = get_column_index_from_alpha_char(square_alg[0])
    row = 8 - int(square_alg[1])
    
    return col, row