import time
import random

from cell import Cell


class Maze:
    def __init__(
        self,
        x1,
        y1, 
        num_rows, 
        num_cols, 
        cell_size_x, 
        cell_size_y, 
        win=None,
        seed=None
        ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        
        if seed:
            random.seed(seed)
        
        print("generating maze..")
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
                
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)
        
        print("generation completed!")
    
    def _create_cells(self):
        self._cells = [[Cell(self._win) for _ in range(self._num_rows)] for _ in range(self._num_cols)]
                
    def _draw_cell(self, i, j):
        if self._win is None:
            return
        x1 = self._x1 + self._cell_size_x * i
        x2 = x1 + self._cell_size_x
        y1 = self._y1 + self._cell_size_y * j
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()
        
    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.04)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._cells[self._num_cols - 1][self._num_rows - 1].has_bottom_wall = False

    def _break_walls_r(self, i, j):
        c = self._cells[i][j]
        c.visited = True
        while True:            
            
            available_directions = []
            if i != 0 and not self._cells[i - 1][j].visited:
                available_directions.append("L")
            if j != 0 and not self._cells[i][j - 1].visited:
                available_directions.append("U")
            if i != self._num_cols - 1 and not self._cells[i + 1][j].visited:
                available_directions.append("R")
            if j != self._num_rows - 1 and not self._cells[i][j + 1].visited:
                available_directions.append("D")
                
            if len(available_directions) == 0:
                #self._draw_cell(i, j)
                return
            
            direction = available_directions[random.randint(0, len(available_directions) - 1)]
            
            match direction:
                case "L":
                    c.has_left_wall = False
                    self._cells[i - 1][j].has_right_wall = False
                    self._break_walls_r(i - 1, j)
                case "U":
                    c.has_top_wall = False
                    self._cells[i][j - 1].has_bottom_wall = False
                    self._break_walls_r(i, j - 1)
                case "R":
                    c.has_right_wall = False
                    self._cells[i + 1][j].has_left_wall = False
                    self._break_walls_r(i + 1, j)
                case "D":
                    c.has_bottom_wall = False
                    self._cells[i][j + 1].has_top_wall = False
                    self._break_walls_r(i, j + 1)
