from graphics import Window, Line, Point


def main():
    
    line = Line(Point(10, 20), Point(600, 200))
    
    win = Window(800, 600)
    win.draw_line(line, "red")
    win.wait_for_close()


if __name__ == "__main__":
    main()
