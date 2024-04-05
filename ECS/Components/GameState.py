from .Component import Component

class GameState(Component):
    def __init__(self):
        self.running = True
        self.game_piece_size = 30