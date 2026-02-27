class Piece:
    def __init__(self, posX: int, posY: int, captured: bool = False):
        self.posX = posX
        self.posY = posY
        self.captured = captured
        self.unmoved = True

    # Check if a move from origin square to target square is valid
    def valid_move(self, oX: int, oY: int, tX: int, tY: int, player: str) -> bool:
        return False

    # Move piece to provided square index
    def move(self, x: int, y: int):
        self.posX = x
        self.posY = y

        if self.unmoved:
            self.unmoved = False
