
class EntityManager:
    def __init__(self):
        self.entities = []

    def add_entity(self, entity):
        self.entities.append(entity)

    def get_by_class(self, class_types):
        return [entity for entity in self.entities if any(isinstance(entity, entity_class) for entity_class in class_types)]
    
    def get_by_component(self, component_types):
        return [entity for entity in self.entities if all(entity.has_component(component_type) for component_type in component_types)]