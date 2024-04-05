class Entity:

    def __init__(self, id):
        self.id = id
        self.components = {}

    def add_component(self, component):
        self.components[type(component)] = component

    def has_component(self, component_type):
        has_comp = any(component == component_type for component in self.components)
        return has_comp
    
    def get_component(self, component_type):
        return self.components.get(component_type)