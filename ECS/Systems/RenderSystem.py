import pygame

from ECS.Components.Transform import *
from ECS.Components.Visibility import *
from Util.Color import *
from ECS.Systems.System import *

class RenderSystem(System):
    def __init__(self, entity_manager):
        super().__init__(entity_manager)
        self.fill_color = Color.WHITE
        self.screen = pygame.display.set_mode((1000, 1000))

   # def start(self):
        #self.__init

    def update(self):
        self.screen.fill(self.fill_color.value)
        for entity in self.entity_manager.get_by_component([Transform, Visibility]):
            visibility = entity.get_component(Visibility)
            transform = entity.get_component(Transform)
            pygame.draw.rect(self.screen, visibility.color.value, (transform.position.x, transform.position.y, transform.scale.x, transform.scale.y))
        pygame.display.flip()
        pygame.time.Clock().tick(60)