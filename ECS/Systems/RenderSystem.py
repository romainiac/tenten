import pygame

from ECS.Components import Transform, Renderable
from Properties import Color
from .System import System

class RenderSystem(System):
    window_width = 600
    window_height = 600
    block_size = 50

    def __init__(self, entity_manager):
        super().__init__(entity_manager)
        self.fill_color = Color.WHITE
        self.screen = pygame.display.set_mode((self.window_width, self.window_height))

    def update(self):
        self.screen.fill(self.fill_color.value)
        for entity in self.entity_manager.get_by_component([Transform, Renderable]):
            renderable = entity.get_component(Renderable)
            transform = entity.get_component(Transform)
            for shape in renderable.shapes:
                pygame.draw.rect(self.screen, shape.color.value, (transform.position.x + shape.x_offset, transform.position.y + shape.y_offset, transform.scale.x, transform.scale.y))
            #self.draw_grid()
            #pygame.draw.rect(self.screen, visibility.color.value, (transform.position.x, transform.position.y, transform.scale.x, transform.scale.y))
        pygame.display.flip()
        pygame.time.Clock().tick(60)

    def draw_grid(self):
        for x in range(0, self.window_width, self.block_size):
            for y in range(0, self.window_height, self.block_size):
                rect = pygame.Rect(x, y, self.block_size, self.block_size)
                pygame.draw.rect(self.screen, Color.BLACK.value, rect, 1)