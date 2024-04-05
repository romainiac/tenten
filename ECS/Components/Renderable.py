from .Component import Component
from Properties import Shape
from typing import Iterable

class Renderable(Component):

    def __init__(self, shapes: Iterable[Shape] = []):
        self.shapes = shapes