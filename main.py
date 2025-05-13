from graphics import Window
from cell import Cell

def main():
    win = Window(800, 800)
    
    c = Cell(win)
    c.has_left_wall = False
    c.draw(100, 100, 200, 200)

    c = Cell(win)
    c.has_right_wall = False
    c.draw(300, 300, 400, 400)

    c = Cell(win)
    c.has_bottom_wall = False
    c.draw(225, 225, 250, 250)

    c = Cell(win)
    c.has_top_wall = False
    c.draw(450, 450, 500, 500)

    win.wait_for_close()

main()