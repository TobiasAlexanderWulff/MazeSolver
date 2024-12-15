from graphics import Window
from maze import Maze


def main():    
    win = Window(800, 600)
    
    maze = Maze(10, 10, 10, 15, 40, 40, win)
    
    win.wait_for_close()


if __name__ == "__main__":
    main()
