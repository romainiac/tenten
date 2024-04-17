from typing import Iterable

class Piece:

    def __init__(self, color, positions: Iterable[tuple]):
        self.color = color
        self.positions = positions