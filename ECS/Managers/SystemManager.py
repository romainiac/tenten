from typing import Iterable
from ECS.Systems import System

class SystemManager:
    def __init__(self, system_list: Iterable[System]):
        self.systems = system_list

    def add_system(self, system: System):
        self.systems.add(system)

    def update_systems(self):
        for system in self.systems:
            system.update()
