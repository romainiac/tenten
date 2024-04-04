class Entity:
    def __init__(self):
        self.components = {}

    def add_component(self, component):
        self.components[type(component)] = component

    def has_component(self, component_type):
        return any(type(component) == type(component_type) for component in self.components)

    def get_component(self, component_type):
        return self.components.get(component_type)