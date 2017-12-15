import tkinter as tk
from PIL import Image, ImageGrab

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

    # print(colorMatrix)

    # some color constants for PIL
    white = (255, 255, 255)
    black = (0, 0, 0)
    blue = (0, 0, 255)
    red = (255, 0, 0)
    green = (0,128,0)

    root = tk.Tk()
    root.title("Score: {}" .format(score))

    frame = tk.Frame()
    frame.pack(fill=tk.BOTH, expand=1)

    canvas = tk.Canvas(frame, width=width, height=height)
    rows, cols = len(colorMatrix[0]), len(colorMatrix)


    # PIL create an empty image and draw object to draw on
    # memory only, not visible
    # image1 = Image.new("RGB", (width, height), white)
    # draw = ImageDraw.Draw(image1)

    #
    rect_width, rect_height = width // rows, height // cols
    for y, row in enumerate(colorMatrix):
        for x, color in enumerate(row):
            x0, y0 = x * rect_width, y * rect_height
            x1, y1 = x0 + rect_width-1, y0 + rect_height-1
            canvas.create_rectangle(x0, y0, x1, y1, fill=color, width=0)
    canvas.pack(fill=tk.BOTH, expand=1)

    canvas.update()

    # canvas.postscript(file="file_name.ps", colormode='color')
    #
    # img = Image.open("file_name.ps")
    # img.save("file_name.png", "png")

    getter(root,canvas,score)

    #root.mainloop()

    #root.exit() # tijdelijk weg
    root.destroy() # voor goed weg

    return(0)


def getter(root,widget,score):
    # after hashes in case of double ppi displays 
    x=root.winfo_rootx()+widget.winfo_x()#x=root.winfo_rootx()*2+widget.winfo_x()
    y=root.winfo_rooty()+widget.winfo_y()#y=root.winfo_rooty()*2+widget.winfo_y()
    x1=x+widget.winfo_width() #* 2
    y1=y+widget.winfo_height() #* 2
    ImageGrab.grab().crop((x,y,x1,y1)).save("export/" + score + ".png")
