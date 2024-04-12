import pygame, random
from Properties import Color
from Board import Board
from Cell import Cell
from Piece import Piece
running = True
WINDOW_H = 800
WINDOW_W = 600
PIECE_SHOW_CENTER = (WINDOW_H / 4, WINDOW_H - 150)
screen = pygame.display.set_mode((WINDOW_W, WINDOW_H))

pygame.init()

pieces = [
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

selected_pieces = []
board = Board(screen, position_x=100,position_y=10,cell_size=40)
board.add_row([Cell(), Cell(), Cell(),Cell(), Cell(), Cell(),Cell(), Cell(), Cell(), Cell()])
board.add_row([Cell(), Cell(), Cell(),Cell(), Cell(), Cell(),Cell(), Cell(), Cell(), Cell()])
board.add_row([Cell(), Cell(), Cell(),Cell(), Cell(), Cell(),Cell(), Cell(), Cell(), Cell()])
board.add_row([Cell(), Cell(), Cell(),Cell(), Cell(), Cell(),Cell(), Cell(), Cell(), Cell()])
board.add_row([Cell(), Cell(), Cell(),Cell(), Cell(), Cell(),Cell(), Cell(), Cell(), Cell()])
board.add_row([Cell(), Cell(), Cell(),Cell(), Cell(), Cell(),Cell(), Cell(), Cell(), Cell()])
board.add_row([Cell(), Cell(), Cell(),Cell(), Cell(), Cell(),Cell(), Cell(), Cell(), Cell()])
board.add_row([Cell(), Cell(), Cell(),Cell(), Cell(), Cell(),Cell(), Cell(), Cell(), Cell()])
board.add_row([Cell(), Cell(), Cell(),Cell(), Cell(), Cell(),Cell(), Cell(), Cell(), Cell()])
board.add_row([Cell(), Cell(), Cell(),Cell(), Cell(), Cell(),Cell(), Cell(), Cell(), Cell()])

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y = pygame.mouse.get_pos()
            if event.button == 1:  # Left mouse button
                board.place(random.choice(pieces))

        screen.fill(Color.WHITE.value)

        while (len(selected_pieces) < 3):
            selected_pieces.append(random.choice(pieces))

    board.draw()
    pygame.display.update()
    pygame.display.flip()
    pygame.time.Clock().tick(60)
