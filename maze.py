from tkinter import Tk, BOTH, Canvas
from shapes.point import Point
from shapes.line import Line
from cells import *
from maze_class import Maze

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze")
        self.__canvas = Canvas(self.__root, width=width, height=height)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.current_cell = None

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()

    def close(self):
        self.__running = False

    def draw_line(self, line, fill_color):
        line.draw(self.__canvas, fill_color)

    def draw_move(self, to_cell, undo=False):
        current_center_x, current_center_y = self.current_cell.get_center()
        next_center_x, next_center_y = to_cell.get_center()
        line = Line(Point(current_center_x, current_center_y), Point(next_center_x, next_center_y))
        if undo:
            self.draw_line(line, "gray")
        else:
            self.draw_line(line, "red")



def main():
    win = Window(800, 600)

    maze = Maze(50, 50, 7, 7, 40, 40, win)

    maze.solve()

    win.wait_for_close()

if __name__ == "__main__":
    main()


