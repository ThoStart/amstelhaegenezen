from class_objects import House, Water, Matrix
import library.setup as info
import library.house_dictionary as hd

def fill(grid, matrix):
    # start in top left corner,
    # move first house accros the whole map check free space on every coordinate
    # remember where most free space around the house, put the house there.

    # calculate free_space
    best_x_cor = 0
    best_y_cor = 0
    best_free_space = 0
    x_coordinate = 30
    y_coordinate = 30

    for hd.house_e_counter in range(1): #range(info.house_m_number):
        for x_coordinate in range(info.grid_width):
            for y_coordinate in range(info.grid_length):
                y_coordinate+=36

                # if house would have been placed onto another house move it
                while matrix.grid[x_coordinate, y_coordinate] != 'v':
                    y_coordinate+=1
                    if(x_coordinate >= info.grid_width and (y_coordinate + 1) >= info.grid_length):
                        x_coordinate+=1

                # place house in top-left corner
                hd.houses_e[hd.house_e_counter] = House(info.house_e_type, ("E{0:02}".format(hd.house_e_counter)), info.house_e_free, info.house_e_value, x_coordinate, y_coordinate, info.house_e_length, info.house_e_width)

                # calculate free space of just placed house
                free_space_actual = matrix.free_space(grid, hd.houses_e[hd.house_e_counter], hd.houses_e[hd.house_e_counter].id, info.house_e_length, info.house_e_width)

                    # replace house if actual free_space is higher than current best free space coordinates
                if (free_space_actual > best_free_space):
                        best_x_cor = x_coordinate
                        print("yolo {}".format(best_x_cor))
                        best_y_cor = y_coordinate
                        print(best_y_cor)
                        best_free_space = free_space_actual

            x_coordinate+=20



    #         matrix.place(info.house_e_length, info.house_e_width, best_x_cor, best_y_cor, hd.houses_e[hd.house_e_counter].id)
    #         hd.house_e_counter+=1
    #         print("success {}".format(hd.houses_e[hd.house_e_counter].id))
