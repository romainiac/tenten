from ECS.Components import Component

class Collider(Component):
    def __init__(self, type):
        self.type = type
