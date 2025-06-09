from shapes.point import Point
from shapes.line import Line

class Cell:
    def __init__(self, Window=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = -1
        self._x2 = -1
        self._y1 = -1
        self._y2 = -1
        self.__win = Window
        self.visited = False

    def draw(self, x1, y1, size):
        if self.__win is None:
            return
        self._x1 = x1
        self._y1 = y1
        self._x2 = x1 + size
        self._y2 = y1 + size
        if self.has_left_wall:
            line = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
            self.__win.draw_line(line, "black")
        else:
            line = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
            self.__win.draw_line(line, "#d9d9d9")
        if self.has_top_wall:
            line = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
            self.__win.draw_line(line, "black")
        else:
            line = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
            self.__win.draw_line(line, "#d9d9d9")
        if self.has_right_wall:
            line = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
            self.__win.draw_line(line, "black")
        else:
            line = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
            self.__win.draw_line(line, "#d9d9d9")
        if self.has_bottom_wall:
            line = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
            self.__win.draw_line(line, "black")
        else:
            line = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
            self.__win.draw_line(line, "#d9d9d9")

    def get_center(self):
        if self._x1 == -1 or self._y1 == -1:
            raise ValueError("Cell hasn't been positioned yet!")
        center_x = self._x1 + 20
        center_y = self._y1 + 20
        return center_x, center_y


