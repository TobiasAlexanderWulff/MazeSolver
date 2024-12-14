from graphics import Window, Line, Point, Cell


def main():    
    win = Window(800, 600)
    cell1 = Cell(Point(10, 10), Point(50, 50), win)
    cell2 = Cell(Point(60, 10), Point(100, 50), win)
    cell2.has_bottom_wall = False
    cell1.draw()
    cell2.draw()
    win.wait_for_close()


if __name__ == "__main__":
    main()
