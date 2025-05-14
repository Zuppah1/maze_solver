from graphics import Window
from cell import Cell
from maze import Maze

def main():
    win = Window(800, 800)

    maze = Maze(50, 50, 14, 14, 50, 50, win)

    win.wait_for_close()

main()