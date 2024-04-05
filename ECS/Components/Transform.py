from .Component import Component
from Properties import Scale, Coordinate

class Transform(Component):
    def __init__(self, 
                 position: Coordinate = Coordinate(0,0), 
                 scale: Scale = Scale(1,1)):
        self.position = position
        self.scale = scale