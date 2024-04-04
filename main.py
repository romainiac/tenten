from enum import Enum

from ECS.Systems import RenderSystem, InputSystem
from ECS.Managers import SystemManager, GameManager, EntityManager
from ECS.Entities import GameState, Entity
from ECS.Components import Coordinate, Scale, Visibility, Transform, Interactable, Collider, ColliderType, Draggable
from Util import Color

game_manager = GameManager()
entity_manager = EntityManager()
game_state = GameState()

#box 1
box1 = Entity()
box1.add_component(Transform(Coordinate(50,50), Scale(50,50)))
box1.add_component(Visibility(Color.BLACK))
box1.add_component(Interactable())
box1.add_component(Draggable())
box1.add_component(Collider(ColliderType.BOX))
entity_manager.add_entity(box1)

#box 2
box1 = Entity()
box1.add_component(Transform(Coordinate(100,50), Scale(50,50)))
box1.add_component(Visibility(Color.BLACK))
box1.add_component(Interactable())
box1.add_component(Draggable())
box1.add_component(Collider(ColliderType.BOX))
entity_manager.add_entity(box1)

entity_manager.add_entity(game_state)


system_manager = SystemManager([RenderSystem(entity_manager),
                                 InputSystem(entity_manager)])

while game_state.running:
    system_manager.update_systems()

game_manager.stop()
