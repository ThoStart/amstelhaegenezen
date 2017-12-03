from class_objects import House, Water, Matrix
import setup as info
import house_dictionary as hd

def fill(grid, matrix):


def rank():
        # calculate value/weight ratio Eengezinswoning
        std_size_e = (info.house_e_width + info.house_e_free) * (info.house_e_length + info.house_e_free)
        value_weight_ratio = info.house_e_value / std_value_e

        print(value_weight_ratio)

        # calculate value/weight ratio Bungalow
        std_size_b = (info.house_b_width + info.house_b_free) * (info.house_b_length + info.house_b_free)
        value_weight_ratio = info.house_e_value / std_value_e

        print(value_weight_ratio)

        # calculate value/weight ratio Bungalow
        std_size_m = (info.house_m_width + info.house_m_free) * (info.house_m_length + info.house_m_free)
        value_weight_ratio = info.house_m_value / std_value_e

        print(value_weight_ratio)

        #rank the optional houses
        # ... SOME CODE MISSING HERE ...

def greedy():
    # start in top left corner,
    # move first house accros the whole map check free space on every coordinate
    # remember where most free space around the house, put the house there.

    # make new house
    hd.counter_e_counter = 1
    hd.houses_e[hd.house_e_counter] = House(info.house_e_type, ("E{0:02}".format(hd.house_e_counter)), info.house_e_free, info.house_e_value, x_coordinate, y_coordinate, info.house_e_length, info.house_e_width)
    # add it to the map
    matrix.place(info.house_e_length, info.house_e_width, x_coordinate, y_coordinate, hd.houses_e[hd.house_e_counter].id)

    # calculate free_space
    best_x_cor = 0
    best_y_cor = 0
    best_free_space = 0

    for x in range(info.grid_width):
        for y in range(info.grid_length):
            while hd.house_e_counter in range(# ... SOME CODE MISSING ...):
                x_coordinate=+1
                y_coordinate=+1

                # if house would have been placed onto another house move it
                if self.grid[x_coordinate, y_coordinate] != 'v':
                    x_coordinate=+1
                    y_coordinate=+1

                if (x_coordinate >= info.grid_length or y_coordinate >= info.grid_width):
                        matrix.place(info.house_e_length, info.house_e_width, best_x_cor, best_y_cor, hd.houses_e[hd.house_e_counter].id)
                        hd.house_e_counter+=1
                        print("success {}".format(hd.houses_e[hd.house_e_counter].id))


                        return # ... SOME CODE MISSING ...

                # place house in top-left corner
                matrix.place(info.house_e_length, info.house_e_width, x_coordinate, y_coordinate, hd.houses_e[hd.house_e_counter].id)

                # calculate free space of just placed house
                free_space_actual = matrix.free_space(grid, hd.houses_m[i], hd.houses_m[i].id, info.house_m_length, info.house_m_width)

                    # replace house if actual free_space is higher than current best free space coordinates
                    elif (free_space_actual > best_free_space)
                        best_x_cor = x_coordinate
                        best_y_cor = y_coordinate
                        best_free_space = matrix.free_space(grid, hd.houses_m[i], hd.houses_m[i].id, info.house_m_length, info.house_m_width)
