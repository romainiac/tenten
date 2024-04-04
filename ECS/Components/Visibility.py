from ECS.Components.Component import *
from Util.Color import *
class Visibility(Component):
    def __init__(self, color: Color = Color.BLACK):
        self.color = color