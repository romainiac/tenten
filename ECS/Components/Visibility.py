from .Component import Component
from Properties import Color

class Visibility(Component):
    def __init__(self, color: Color = Color.BLACK):
        self.color = color