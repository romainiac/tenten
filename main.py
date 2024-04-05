from enum import Enum
from ECS.Managers import GameManager

game_manager = GameManager()

game_manager.start_game()
while game_manager.is_running():
    game_manager.update_systems()
game_manager.destroy()
