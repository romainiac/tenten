import pygame
from Properties import Color
from Cell import Cell
from typing import Iterable
import time
from Piece import Piece

class Board:

    def __init__(self, screen, position_x, position_y, cell_size, color: Color = Color.BLACK):
        self.screen = screen
        self.clearing = False
        self.position_x = position_x
        self.position_y = position_y
        self.rows = []
        self.cell_size = cell_size
        self.color = color
        self.score = 0

    def add_row(self, row: Iterable[Cell]):
        i = len(self.rows)
        y1 = self.position_y + (i * self.cell_size)
        y2 = y1 + self.cell_size
        for j, cell in enumerate(row):
            x1 = self.position_x + (j * self.cell_size)
            x2 = x1 + self.cell_size
            cell.update_location(x1,y1,x2,y2)
        self.rows.append(row)


    def find_valid_places(self, piece: Piece):
        valid_places = []
        for i, row in enumerate(self.rows):
            for j, cell in enumerate(row):
                valid = self._can_place(i,j, piece)
                if valid:
                    valid_places.append((i,j))
        return valid_places

    def place(self, piece: Piece, pos):
        if not self.clearing:
            #found_pos = self._find_place(piece)
            for row_idx, piece_row in enumerate(piece.positions):
                next_place = (pos[0] + piece_row[0],pos[1]+ piece_row[1])
                to_change = self.rows[next_place[0]][next_place[1]]
                to_change.color = piece.color
                to_change.filled = True
                self.score += 1
        else:
            print("wait to clear")

    def _clear_rows(self):
        # mark rows to clear
        for i, row in enumerate(self.rows):
            filled = True
            for j, cell in enumerate(row):
                if not cell.filled:
                    filled = False
            if filled:
                for j, cell in enumerate(row):
                    cell.clear = True
                    cell.clear_time = j * 2

        # mark columns to clear
        for i in range(0, len(self.rows[0])):
            filled = True
            for j in range(0, len(self.rows)):
                cell = self.rows[j][i]
                if not cell.filled:
                    filled = False
            if filled:
                for j in range(0, len(self.rows)):
                    cell = self.rows[j][i]
                    cell.clear = True
                    cell.clear_time = j * 2

        # clear
        cleared = True
        current_score = 0
        for i, row in enumerate(self.rows):
            for j, cell in enumerate(row):
                if cell.clear:
                    cleared = False
                    if cell.animate_ticks >= cell.clear_time:
                        current_score += 1
                        cell.reset()
                    else:
                        cell.animate_ticks  += 1
        self.score += current_score
        self.clearing = not cleared

    def _can_place(self, pos_x, pos_y, piece: Piece):
        for place in piece.positions:
            x = place[0] + pos_x
            y = place[1] + pos_y
            if x >= len(self.rows):
                return False
            if y >= len(self.rows[x]):
                return False
            if self.rows[x][y].filled:
                return False
        return True

    def _handle_click(self, mouse_pos_x, mouse_pos_y):
        for i, row in enumerate(self.rows):
            for j, cell in enumerate(row):
                if self._is_mouse_colliding(cell, mouse_pos_x, mouse_pos_y):
                    pass
                    #cell.color = Color.BLACK

    def _is_mouse_colliding(self, cell: Cell, mouse_x, mouse_y):
        return cell.x1 <= mouse_x <= cell.x2 and cell.y1 <= mouse_y <= cell.y2

    def draw(self, selected_pieces):
        for i, row in enumerate(self.rows):
            for j, cell in enumerate(row):
                cell_position_x = self.position_x + (j * self.cell_size)
                cell_position_y = self.position_y + (i * self.cell_size)
                pygame.draw.rect(self.screen, cell.color.value, (cell_position_x, cell_position_y, self.cell_size, self.cell_size))
            self._draw_horizontal_lines()
            self._draw_vertical_lines()
        self._clear_rows()
        self._draw_selected_pieces(selected_pieces)
            #self._draw_coordinates()
        
    def _draw_selected_pieces(self, selected_pieces):
        board_w = self.position_x + (len(self.rows) * self.cell_size)
        board_h = self.position_y + (len(self.rows[0]) * self.cell_size)
        for i, piece in enumerate(selected_pieces):
            for j, coord in enumerate(piece.positions):
                y,x = coord
                position_x = self.position_x + (x * self.cell_size / 2) + (i * board_w / 3)
                position_y = self.position_y  + 500 + (y * self.cell_size / 2)
                pygame.draw.rect(self.screen, piece.color.value, (position_x, position_y, self.cell_size / 2, self.cell_size / 2))

    def _draw_coordinates(self):
        font=pygame.font.SysFont('timesnewroman',  30)
        for i, row in enumerate(self.rows):
            for j, cell in enumerate(row):
                text_surface = font.render(str(i + j), True, Color.BLACK.value)  # Render text with black color
                text_rect = text_surface.get_rect(center=((cell.x1 + cell.x2)/2, (cell.y1 + cell.y2) / 2))  # Center the text
                self.screen.blit(text_surface, text_rect)  # Draw the text on the screen
                
    def _draw_horizontal_lines(self):
        col_count = 0
        row_count = len(self.rows)
        if row_count > 0:
            col_count = len(self.rows[0])
        for i in range(0, row_count + 1):
            line_length = col_count * self.cell_size
            x1 = self.position_x
            x2 = x1 + line_length
            y1 = self.position_y + (i * self.cell_size)
            y2 = y1
            pygame.draw.line(self.screen, self.color.value, (x1,y1), (x2,y2))

        for i, row in enumerate(self.rows):
            line_length = len(row) * self.cell_size
            x1 = self.position_x
            x2 = x1 + line_length
            y1 = self.position_y + (i * self.cell_size)
            y2 = y1
            pygame.draw.line(self.screen, self.color.value, (x1,y1), (x2,y2))

    def _draw_vertical_lines(self):
        col_count = 0
        row_count = len(self.rows)
        if row_count > 0:
            col_count = len(self.rows[0])
        for i in range(0, col_count + 1):
            line_length = row_count * self.cell_size
            x1 = self.position_x + (i * self.cell_size)
            x2 = x1
            y1 = self.position_y
            y2 = y1 + line_length
            pygame.draw.line(self.screen, self.color.value, (x1,y1), (x2,y2))
        