
from .Piece import Piece

class Grid:

    def __init__(self, rows: int, cols: int, cell_size: int):
        self.rows = rows
        self.cols = cols
        self.cell_size = cell_size
        self.clear()

    def clear(self):
        self.grid = [[0 for j in range(self.cols)] for i in range(self.rows)]  

    def get_valid_places(self, piece: Piece):
        valid_places = []
        for i, row in enumerate(self.grid):
            for j, cell in enumerate(row):
                valid = self._can_place(i,j, piece)
                if valid:
                    valid_places.append((i,j))
        return valid_places
    
    def _clear_rows(self):
        score = 0

        # clear rows
        for i, row in enumerate(self.grid):
            filled = True
            for j, cell in enumerate(row):
                if cell == 0:
                    filled = False
            if filled:
                for j, cell in enumerate(row):
                    score += 1
                    self.grid[i][j] = 0

        # clear columns
        for i in range(0, self.cols):
            filled = True
            for j in range(0, self.rows):
                cell = self.grid[j][i]
                if cell == 0:
                    filled = False
            if filled:
                for j in range(0, self.rows):
                    score += 1
                    self.grid[j][i] = 0
        return score
    
    def place(self, piece: Piece, pos):
        score = 0
        for row_idx, piece_row in enumerate(piece.positions):
            score += 1
            next_place = (pos[0] + piece_row[0],pos[1]+ piece_row[1])
            self.grid[next_place[0]][next_place[1]] = piece.color.value
        score += self._clear_rows()
        return score
    
    def _can_place(self, pos_x, pos_y, piece: Piece):
        for place in piece.positions:
            x = place[0] + pos_x
            y = place[1] + pos_y
            if x >= self.rows:
                return False
            if y >= self.cols:
                return False
            if self.grid[x][y] != 0:
                return False
        return True

    