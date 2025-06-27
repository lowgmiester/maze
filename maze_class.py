from cells import Cell
import random
import time

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self.__cells = []
        self.seed = seed
        if seed:
            random.seed(seed)

        self.__create_cells()

        print(len(self.__cells))
        print(len(self.__cells[0]))

        self.__break_entrance_and_exit()
        self.__break_walls_r(0, 0)
        self.__reset_cells_visited()


    def __create_cells(self):
        for i in range(self.num_rows):
            c_row = []
            for j in range(self.num_cols):
                c_row.append(Cell(self.win))
            self.__cells.append(c_row)
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                self.__draw_cell(i, j)

    def __draw_cell(self, i, j):
        if self.win is None:
            return
        x1 = self.x1 + j * self.cell_size_x
        y1 = self.y1 + i * self.cell_size_y
        self.__cells[i][j].draw(x1, y1, self.cell_size_x)
        self.__animate()

    def __animate(self):
        if self.win is None:
            return
        self.win.redraw()
        time.sleep(0.05)

    def __break_entrance_and_exit(self):
        start_c = self.__cells[0][0]
        start_c.has_top_wall = False
        self.__draw_cell(0, 0)
        end_c = self.__cells[-1][-1]
        end_c.has_bottom_wall = False
        self.__draw_cell(self.num_rows - 1, self.num_cols - 1)

    def __break_walls_r(self, i, j):
        self.__cells[i][j].visited = True
        while True:
            to_do = []
            directions = [
                (-1, 0),  # Up
                (1, 0),   # Down
                (0, -1),  # Left
                (0, 1)    # Right
            ]
            for dir in directions:
                new_i = i + dir[0]
                new_j = j + dir[1]
                if new_i >= 0 and new_i < self.num_rows:
                    if new_j >= 0 and new_j < self.num_cols:
                        if not self.__cells[new_i][new_j].visited:
                            to_do.append([new_i, new_j])
            if len(to_do) == 0:
                self.__draw_cell(i, j)
                return
            else:
                next_i, next_j = random.choice(to_do)
                if next_i < i: # above
                    self.__cells[i][j].has_top_wall = False
                    self.__cells[next_i][next_j].has_bottom_wall = False
                elif next_i > i: # below
                    self.__cells[i][j].has_bottom_wall = False
                    self.__cells[next_i][next_j].has_top_wall = False
                elif next_j < j: # to the left
                    self.__cells[i][j].has_left_wall = False
                    self.__cells[next_i][next_j].has_right_wall = False
                elif next_j > j: # to the right
                    self.__cells[i][j].has_right_wall = False
                    self.__cells[next_i][next_j].has_left_wall = False
                self._Maze__break_walls_r(next_i, next_j)

    def __reset_cells_visited(self):
        for row in self.__cells:
            for cell in row:
                cell.visited = False

    def solve(self):
        return self._solve_r(i=0, j=0)

    def _solve_r(self, i, j):
        self.__animate()
        self.__cells[i][j].visited = True
        if (i, j) == (self.num_rows - 1, self.num_cols - 1):
            return True
        directions = [
            (-1, 0),  # Up
            (1, 0),   # Down
            (0, -1),  # Left
            (0, 1)    # Right
        ]


        for dir in directions:
            new_i = i + dir[0]
            new_j = j + dir[1]

            if new_i >= 0 and new_i <= self.num_rows - 1 and new_j >= 0 and new_j <= self.num_cols - 1:
                if (
                    dir == directions[0]
                    and self.__cells[i][j].has_top_wall == False
                    and self.__cells[new_i][new_j].has_bottom_wall == False
                ):
                    if self.__cells[new_i][new_j].visited == False:
                        self.win.current_cell = self.__cells[i][j]
                        self.win.draw_move(self.__cells[new_i][new_j])
                        result = self._solve_r(new_i, new_j)
                        if result == True:
                            return True
                        else:
                            self.win.current_cell = self.__cells[i][j]
                            self.win.draw_move(self.__cells[new_i][new_j], undo=True)
                elif (
                    dir == directions[1]
                    and self.__cells[i][j].has_bottom_wall == False
                    and self.__cells[new_i][new_j].has_top_wall == False
                ):
                    if self.__cells[new_i][new_j].visited == False:
                        self.win.current_cell = self.__cells[i][j]
                        self.win.draw_move(self.__cells[new_i][new_j])
                        result = self._solve_r(new_i, new_j)
                        if result == True:
                            return True
                        else:
                            self.win.current_cell = self.__cells[i][j]
                            self.win.draw_move(self.__cells[new_i][new_j], undo=True)
                elif (
                    dir == directions[2]
                    and self.__cells[i][j].has_left_wall == False
                    and self.__cells[new_i][new_j].has_right_wall == False
                ):
                    if self.__cells[new_i][new_j].visited == False:
                        self.win.current_cell = self.__cells[i][j]
                        self.win.draw_move(self.__cells[new_i][new_j])
                        result = self._solve_r(new_i, new_j)
                        if result == True:
                            return True
                        else:
                            self.win.current_cell = self.__cells[i][j]
                            self.win.draw_move(self.__cells[new_i][new_j], undo=True)
                elif (
                    dir == directions[3]
                    and self.__cells[i][j].has_right_wall == False
                    and self.__cells[new_i][new_j].has_left_wall == False
                ):
                    if self.__cells[new_i][new_j].visited == False:
                        self.win.current_cell = self.__cells[i][j]
                        self.win.draw_move(self.__cells[new_i][new_j])
                        result = self._solve_r(new_i, new_j)
                        if result == True:
                            return True
                        else:
                            self.win.current_cell = self.__cells[i][j]
                            self.win.draw_move(self.__cells[new_i][new_j], undo=True)


        return False







