from ECS.Entities import Entity

class GameState(Entity):
    def __init__(self):
        super().__init__()
        self.running = True