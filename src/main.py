from graphics import Window
from cell import Cell


def main():    
    win = Window(800, 600)
    
    cell1 = Cell(win)
    cell1.draw(10, 10, 50, 50)
    
    cell2 = Cell(win)
    cell2.has_bottom_wall = False
    cell2.draw(60, 10, 100, 50)
    
    cell1.draw_move(cell2, True)
    
    win.wait_for_close()


if __name__ == "__main__":
    main()
