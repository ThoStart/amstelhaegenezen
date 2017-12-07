import tkinter as tk

def create(mtrx, grd, score):

    class Level:
        def __init__(self, name, height, width):
            self.name = name
            self.height = height
            self.width = width
            self.tiles = makeTiles(height, width)

        class Tile:
            def __init__(self, x, y, type, color):
                self.x = x
                self.y = y
                self.type = type
                self.color = color


    def makeLevel(name, height, width):
        level = Level(name, height, width)
        return level

    def makeTiles(height, width):
        tiles = [[Level.Tile(x, y, "Surface", "Green") for x in range(width)] for y in range(height)]
        return tiles

    test1 = makeLevel("test", mtrx.xsize, mtrx.ysize)
    for x in range(test1.height):
        for y in range(test1.width):
            if 'E' in mtrx.grid[x, y]:
                test1.tiles[x][y].color = "Yellow"
            if 'B' in mtrx.grid[x, y]:
                test1.tiles[x][y].color = "Orange"
            if 'M' in mtrx.grid[x, y]:
                test1.tiles[x][y].color = "Red"
            if '~' in mtrx.grid[x, y]:
                test1.tiles[x][y].color = "Blue"

    colorMatrix = [[0 for x in range(test1.width)] for y in range(test1.height)]
    for x in range(test1.height):
        for y in range(test1.width):
            colorMatrix[x][y] = test1.tiles[x][y].color

    width, height = test1.width, test1.height

    root = tk.Tk()
    root.title("Score: {}" .format(score))

    frame = tk.Frame()
    frame.pack(fill=tk.BOTH, expand=1)

    canvas = tk.Canvas(frame, width=width, height=height)
    rows, cols = len(colorMatrix[0]), len(colorMatrix)

    rect_width, rect_height = width // rows, height // cols
    for y, row in enumerate(colorMatrix):
        for x, color in enumerate(row):
            x0, y0 = x * rect_width, y * rect_height
            x1, y1 = x0 + rect_width-1, y0 + rect_height-1
            canvas.create_rectangle(x0, y0, x1, y1, fill=color, width=0)
    canvas.pack(fill=tk.BOTH, expand=1)

    root.mainloop()

    return(0)
