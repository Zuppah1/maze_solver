import time
import random
from cell import Cell
from graphics import Window


class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win

        if seed:
            random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()

        self._break_walls_r(0, 0)
        self._reset_cells_visited()
        self.solve()

    def solve(self):
        return self._solve_r(0, 0)
    
    def _solve_r(self, i, j):
        self._animate()
        self._cells[i][j].visited = True
        end_cell = self._cells[-1][-1]
        if self._cells[i][j] == end_cell:
            return True
        
        # left
        if i > 0 and not self._cells[i - 1][j].visited and not self._cells[i][j].has_left_wall:
            self._cells[i][j].draw_move(self._cells[i - 1][j])
            move = self._solve_r(i - 1, j)
            if move:
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i - 1][j], True)

        # right
        if i < self._num_cols - 1 and not self._cells[i + 1][j].visited and not self._cells[i][j].has_right_wall:
            self._cells[i][j].draw_move(self._cells[i + 1][j])
            move = self._solve_r(i + 1, j)
            if move:
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i + 1][j], True)

        # up
        if j > 0 and not self._cells[i][j - 1].visited and not self._cells[i][j].has_top_wall:
            self._cells[i][j].draw_move(self._cells[i][j - 1])
            move = self._solve_r(i, j - 1)
            if move:
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j - 1], True)

        # down
        if j < self._num_rows - 1 and not self._cells[i][j + 1].visited and not self._cells[i][j].has_bottom_wall:
            self._cells[i][j].draw_move(self._cells[i][j + 1])
            move = self._solve_r(i, j + 1)
            if move:
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j + 1], True)

        return False


        

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
 
        while True:
            to_visit = []

            # left
            if i > 0 and not self._cells[i - 1][j].visited:
                to_visit.append((i - 1, j))

            # right
            if i < self._num_cols - 1 and not self._cells[i + 1][j].visited:
                to_visit.append((i + 1, j))

            # up
            if j > 0 and not self._cells[i][j - 1].visited:
                to_visit.append((i, j - 1))

            # down
            if j < self._num_rows - 1 and not self._cells[i][j + 1].visited:
                to_visit.append((i, j + 1))
            
            if not to_visit:
                self._draw_cell(i, j)
                return
            else:
                direction = random.choice(to_visit)
                if direction[0] == i + 1 and direction[1] == j:
                    self._cells[direction[0]][direction[1]].has_left_wall = False
                    self._cells[i][j].has_right_wall = False
                    

                elif direction[0] == i and direction [1] == j + 1:
                    self._cells[direction[0]][direction[1]].has_top_wall = False
                    self._cells[i][j].has_bottom_wall = False
                    

                elif direction[0] == i - 1 and direction [1] == j:
                    self._cells[direction[0]][direction[1]].has_right_wall = False
                    self._cells[i][j].has_left_wall = False
                    

                elif direction[0] == i and direction [1] == j - 1:
                    self._cells[direction[0]][direction[1]].has_bottom_wall = False
                    self._cells[i][j].has_top_wall = False
                    

                self._break_walls_r(direction[0], direction[1])

    def _reset_cells_visited(self):
        for col in self._cells:
            for cell in col:
                cell.visited = False

    def _create_cells(self):
        self._cells = []
        for i in range(0, self._num_cols):
            column = []
            for j in range(0, self._num_rows):
                cell = Cell(self._win)
                column.append(cell)
            self._cells.append(column)
        for i in range(0, self._num_cols):
            for j in range(0, self._num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        x1 = self._x1
        y1 = self._y1
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y

        self._cells[i][j].draw(
            (x1 + (self._cell_size_x * i)), (y1 + (self._cell_size_y * j)),
            (x2 + (self._cell_size_x * i)), (y2 + (self._cell_size_y * j))
        )

        self._animate()

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[-1][-1].has_bottom_wall = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)

    def _animate(self):
        if self._win:
            self._win.redraw()
            time.sleep(0.0005)



