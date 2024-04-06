from Properties import Color
class Cell:

    def __init__(self, color: Color = Color.WHITE, filled: bool = False):
        self.color = color
        self.filled = filled

    def update_location(self, x1,y1,x2,y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
