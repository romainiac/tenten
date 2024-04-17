import pygame
from .Piece import Piece
from .PlayablePieces import PlayablePieces
from Properties import Color, DarkTheme
from .Grid import Grid
from .GameStats import GameStats
from .Renderer import Renderer
import random

class GameManager:

    def __init__(self):
        pygame.init()
        self.running = True
        self.game_lost = False
        self.playable_pieces = PlayablePieces()
        self.grid = Grid(10,10,30)
        self.game_stats = GameStats()
        self.window_h = 800
        self.window_w = 600
        self.screen = pygame.display.set_mode((self.window_w, self.window_h))
        self.renderer = Renderer(self.screen, 
                    grid=self.grid, 
                    game_stats=self.game_stats,
                    playable_pieces=self.playable_pieces,
                    window_w=self.window_w, 
                    window_h=self.window_h, 
                    theme=DarkTheme())
        self.pieces = [
            Piece(Color.GREEN, [
                (0,0),
                (0,1),
                (0,2),
                (1,0),
                (1,1),
                (1,2),
                (2,0),
                (2,1),
                (2,2)
            ]),
            Piece(Color.RED, [
                (0,0),
                (0,1),
                (0,2),
                (0,3),
                (0,4),
            ]),
            Piece(Color.RED, [
                (0,0),
                (1,0),
                (2,0),
                (3,0),
                (4,0),
            ]),
            Piece(Color.ORANGE, [
                (0,0),
                (1,0),
                (2,0)
            ]),
            Piece(Color.YELLOW, [
                (0,0),
                (0,1)
            ]),
            Piece(Color.LIGHT_GREEN, [
                (0,0),
                (0,1),
                (1,0),
                (1,1)
            ]),
            Piece(Color.PURPLE, [
                (0,0),
            ]),
            Piece(Color.LIGHT_BLUE, [
                (0,0),
                (0,1),
                (0,2),
                (1,2),
                (2,2)
            ]),
        ]

    def _start_new_game(self):
        self.game_lost = False
        self.playable_pieces.pieces = []
        self._update_playable_pieces()
        self.grid.clear()
        self.game_stats.score = 0
        self.game_stats.games_played += 1

    def update(self):
        self.renderer.draw()
        if self.game_lost:
            self._start_new_game()

        self._update_playable_pieces()

        for event in pygame.event.get():
            # input
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # Left mouse button
                        self._play()
        self._play()
        pygame.display.update()
        pygame.display.flip()
        pygame.time.Clock().tick(60)

    def _play(self):
        move = self._choose_move()
        if move:
            move_piece, move_pos = move
            score = self.grid.place(move_piece, move_pos)
            self.game_stats.score += score
            if self.game_stats.score > self.game_stats.highest_score:
                self.game_stats.highest_score = self.game_stats.score
            self.playable_pieces.pieces.remove(move_piece)
            if not self._choose_move() and len(self.playable_pieces.pieces) > 0:
                self.game_lost = True
        else:
            self.game_lost = True
        

    def _choose_move(self):
        moves = self._get_moves()
        if len(moves) == 0:
            return None
        return random.choice(moves)

    def _get_moves(self):
        moves = []
        for piece in self.playable_pieces.pieces:
            for place in self.grid.get_valid_places(piece):
                moves.append((piece, place))
        return moves
                
    def _update_playable_pieces(self):
        if len(self.playable_pieces.pieces) == 0:
            self.playable_pieces.pieces = random.choices(self.pieces, k=3)

