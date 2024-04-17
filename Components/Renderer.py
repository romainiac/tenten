from Properties import Theme, DarkTheme
from .Grid import Grid
from .Piece import Piece
from .PlayablePieces import PlayablePieces
from .GameStats import GameStats
import pygame
from typing import Iterable

class Renderer:

    def __init__(self, screen, 
                 window_w: int, 
                 window_h: int, 
                 game_stats: GameStats,
                 grid: Grid,
                 playable_pieces: PlayablePieces,
                 title: str = "1010!", 
                 theme: Theme = DarkTheme):
        self.screen = screen
        self.game_stats = game_stats
        self.grid = grid
        self.playable_pieces = playable_pieces
        self.window_w = window_w
        self.window_h = window_h
        self.window_center_x = window_w / 2
        self.window_center_y = window_h / 2
        self.title = title
        self.theme = theme

    def draw(self):
        self.screen.fill(self.theme.color_setting.primary.value)
        self._draw_grid()
        self._draw_pieces()
        #self._draw_title()
        self._draw_score()

    def _draw_title(self):
        text_surface = self.theme.font_setting.primary.render(self.title, True, self.theme.color_setting.title.value)
        text_rect = text_surface.get_rect(center=((300, 70)))
        self.screen.blit(text_surface, text_rect)

    def _draw_score(self):
        text_surface = self.theme.font_setting.primary.render(str(self.game_stats.score), True, self.theme.color_setting.title.value)
        text_rect = text_surface.get_rect(center=((300, 70)))
        self.screen.blit(text_surface, text_rect)   

        text_surface = self.theme.font_setting.primary.render("Highest: " + str(self.game_stats.highest_score), True, self.theme.color_setting.title.value)
        text_rect = text_surface.get_rect(center=((300, 150)))
        self.screen.blit(text_surface, text_rect)       

        text_surface = self.theme.font_setting.primary.render("Games Played: " + str(self.game_stats.games_played), True, self.theme.color_setting.title.value)
        text_rect = text_surface.get_rect(center=((300, 200)))
        self.screen.blit(text_surface, text_rect)               

    def _draw_pieces(self):
        grid_center_x = self.grid.rows / 2 * self.grid.cell_size
        grid_center_y = self.grid.cols / 2 * self.grid.cell_size
        h = self.grid.rows * self.grid.cell_size
        w = self.grid.cols * self.grid.cell_size
        offset_y = grid_center_y + (self.grid.rows * self.grid.cell_size)
        rect = pygame.Rect(grid_center_x, grid_center_y + offset_y, w, h / 2)
        pygame.draw.rect(self.screen, self.theme.color_setting.secondary.value, rect)

        for i, piece in enumerate(self.playable_pieces.pieces):
            for j, coord in enumerate(piece.positions):
                y,x = coord
                position_x = 20 + (i * 100) + grid_center_x  + (x * self.grid.cell_size / 2)
                position_y = grid_center_y + offset_y + 20 + (y * self.grid.cell_size / 2)
                pygame.draw.rect(self.screen, piece.color.value, (position_x, position_y, self.grid.cell_size / 2, self.grid.cell_size / 2))

    def _draw_grid(self):
        grid_center_x = self.grid.rows / 2 * self.grid.cell_size
        grid_center_y = self.grid.cols / 2 * self.grid.cell_size
        for i, row in enumerate(self.grid.grid):
            for j, col in enumerate(row):
                x = (j * self.grid.cell_size) + 1 + self.window_center_x - grid_center_x
                y = i * self.grid.cell_size + 1 + self.window_center_y - grid_center_y
                rect = pygame.Rect(x, y, self.grid.cell_size -1, self.grid.cell_size -1)
                color = self.theme.color_setting.secondary.value
                if col != 0:
                    color = col
                pygame.draw.rect(self.screen, color, rect)
