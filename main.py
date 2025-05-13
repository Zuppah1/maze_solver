from graphics import Window, Line, Point

def main():
    win = Window(800, 800)
    line = Line(Point(100, 100), Point(500, 500))
    win.draw_line(line, "red")

    win.wait_for_close()

main()