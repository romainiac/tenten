from .Color import Color

class Shape:
    def __init__(self, color: Color, width: float = 1, height: float = 1, x_offset: float = 0, y_offset: float = 0):
        self.color = color
        self.width = width
        self.height = height
        self.x_offset = x_offset
        self.y_offset = y_offset
