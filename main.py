import pygame
from Components import Grid, Renderer, GameManager
from Properties import DarkTheme

game_manager = GameManager()

while game_manager.running:
    game_manager.update()
