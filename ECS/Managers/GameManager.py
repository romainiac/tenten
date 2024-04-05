import pygame, sys, random
from .EntityManager import EntityManager
from .SystemManager import SystemManager
from ECS.Systems import RenderSystem, InputSystem
from ECS.Components import GameState, Transform, Renderable, Interactable, Draggable, Collider
from Properties import Shape, Scale, Color, Coordinate, ColliderType, GamePiece

class GameManager:
    def __init__(self):
        pygame.init()

    def start_game(self):
        self.entity_manager = EntityManager()
        self.game_state = self.entity_manager.add_entity()
        self.game_state.add_component(GameState())
        self.system_manager = SystemManager([RenderSystem(self.entity_manager),
                                 InputSystem(self.entity_manager)])
        self.initialize_game_pieces()
        
    def initialize_game_pieces(self):
        game_piece_size = self.game_state.get_component(GameState).game_piece_size
        box1 = self.entity_manager.add_entity()
        box1.add_component(Transform(Coordinate(50,50), Scale(game_piece_size,game_piece_size)))
        box1.add_component(Renderable(shapes=self.get_random_shape(game_piece_size)))
        box1.add_component(Interactable())
        box1.add_component(Draggable())
        box1.add_component(Collider(ColliderType.RENDERED))

    def get_random_shape(self, game_piece_size):
        options = []
        options.append(GamePiece(Color.RED, [(0,0), (0,1), (1,0), (1,1)])) # box
        options.append(GamePiece(Color.BLUE, [(0,0),(0,1),(0,2)])) # 3 line horizontal
        options.append(GamePiece(Color.GREEN, [(0,0)])) # dot
        options.append(GamePiece(Color.BLACK, [(0,0),(1,0),(1,1)])) # left hook
        shapes = []
        piece = random.choice(options)
        for position in piece.positions:
            shapes.append(Shape(piece.color, x_offset=position[0] * game_piece_size, y_offset=position[1] * game_piece_size))
        return shapes
        #shapes = [Shape(Color.RED), Shape(Color.RED, x_offset=game_piece_size), Shape(Color.RED, y_offset=game_piece_size)]

    def update_systems(self):
        self.system_manager.update_systems()

    def is_running(self):
        return self.game_state.get_component(GameState).running

    def destroy(self):
        pygame.quit()
        sys.exit()