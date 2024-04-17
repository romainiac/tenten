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
board = Board(screen, position_x=100,position_y=100,cell_size=40)
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

def place_piece():
    valid_piece_and_board_pos = []
    for piece in selected_pieces:
        valid_places = board.find_valid_places(piece)
        if len(valid_places) > 0:
            valid_piece_and_board_pos.append((piece, valid_places))

    if len(valid_piece_and_board_pos) == 0:
        return False
    else:
        selected_piece, selected_board_pos = random.choice(valid_piece_and_board_pos)
        selected_pos = random.choice(selected_board_pos)
        selected_pieces.remove(selected_piece)
        board.place(selected_piece, selected_pos)
    return True

font=pygame.font.SysFont('timesnewroman',  30)
game_lost = False
while running:
    for event in pygame.event.get():

        if (len(selected_pieces) == 0):
            selected_pieces = random.choices(pieces, k=3)
        
        # input
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if not game_lost:
                mouse_x,mouse_y = pygame.mouse.get_pos()
                if event.button == 1:  # Left mouse button
                    if not place_piece():
                        game_lost = True

    screen.fill(Color.WHITE.value)

    text_surface = font.render(str(board.score), True, Color.BLACK.value)
    text_rect = text_surface.get_rect(center=((300, 90)))
    screen.blit(text_surface, text_rect)

    if game_lost:
        text_surface = font.render("Game Lost", True, Color.BLACK.value)
        text_rect = text_surface.get_rect(center=((300, 70)))
        screen.blit(text_surface, text_rect)

    board.draw(selected_pieces)
    pygame.display.update()
    pygame.display.flip()
    pygame.time.Clock().tick(60)
