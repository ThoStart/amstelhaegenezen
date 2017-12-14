from classes.class_objects import House, Water, Matrix
import library.setup as info

# use matplotlib to visualize normal distribution graph
def fill(matrix, grid, water_layout):

    if water_layout == 1:
        # water in two corners
        matrix.place(int(info.water_length / 2), info.water_width * 2, 0, 0, "~")
        matrix.place(int(info.water_length * 1.5), int(info.water_width / 1.5), int(info.water_length / 2), 0, "~")
        matrix.place(int(info.water_length / 2), info.water_width * 2, info.grid_length-int(info.water_length / 2), info.grid_width-info.water_width * 2, "~")
        matrix.place(int(info.water_length * 1.5), int(info.water_width / 1.5), info.grid_length - int(info.water_length * 1.5) - int(info.water_length / 2), info.grid_width-int(info.water_length / 1.5), "~")

    else:
        # water in four corners
        matrix.place(info.water_length, info.water_width, 0, 0, "~")
        matrix.place(info.water_length, info.water_width, info.grid_length-info.water_length, 0, "~")
        matrix.place(info.water_length, info.water_width, 0, info.grid_width-info.water_width, "~")
        matrix.place(info.water_length, info.water_width, info.grid_length-info.water_length, info.grid_width-info.water_width, "~")
