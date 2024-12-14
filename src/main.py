from graphics import Window, Line, Point


def main():    
    win = Window(800, 600)
    line = Line(Point(10, 20), Point(600, 200))
    win.draw_line(line, "red")
    win.wait_for_close()


if __name__ == "__main__":
    main()
