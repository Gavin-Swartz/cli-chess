class Piece:
    def __init__(self, posX: int, posY: int, captured: bool = False):
        self.posX = posX
        self.posY = posY
        self.captured = captured

    def move(self, newX, newY):
        self.posX = newX
        self.posY = newY
