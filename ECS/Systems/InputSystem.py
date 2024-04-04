from .System import System
from ECS.Components import Interactable, Collider, Transform, ColliderType, Visibility, Draggable
from ECS.Entities import GameState
from Util import Color
import pygame

class InputSystem(System):
    mouse_x,mouse_y = 0,0

    def __init__(self, entity_manager):
        super().__init__(entity_manager)

    def update(self):
        self.mouse_x,self.mouse_y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_state = self.entity_manager.get_by_class([GameState])
                if len(game_state) > 0: 
                    game_state[0].running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    self.handle_left_click()
            elif event.type == pygame.MOUSEBUTTONUP:
                self.handle_mouse_up()
            elif event.type == pygame.MOUSEMOTION:
                self.handle_mouse_motion()

    def handle_mouse_up(self):
        entities = self.entity_manager.get_by_component([Draggable])
        for entity in entities:
            draggable = entity.get_component(Draggable)
            if draggable:
                draggable.dragging = False  
    def handle_mouse_motion(self):
        entities = self.entity_manager.get_by_component([Interactable, Collider, Transform, Draggable])
        for entity in entities:
            draggable = entity.get_component(Draggable)
            if draggable and draggable.dragging:
                transform = entity.get_component(Transform)
                transform.position.x =  self.mouse_x - transform.scale.x / 2
                transform.position.y = self.mouse_y - transform.scale.y / 2    

    def handle_left_click(self):
        entities = self.entity_manager.get_by_component([Interactable, Collider, Transform, Draggable])
        for entity in entities:
            if self.is_mouse_colliding(entity):
                draggable = entity.get_component(Draggable)
                if draggable:
                    draggable.dragging = True  

    def is_mouse_colliding(self, entity):
        collider = entity.get_component(Collider)
        transform = entity.get_component(Transform)
        if collider.type == ColliderType.BOX:
            return transform.position.x <= self.mouse_x <= transform.position.x + transform.scale.x and transform.position.y <= self.mouse_y <= transform.position.y + transform.scale.y
        return False
                


