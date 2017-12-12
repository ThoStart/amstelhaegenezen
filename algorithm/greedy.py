from classes.class_objects import House, Water, Matrix
import library.setup as info
import library.house_dictionary as hd

def fill_old(grid, matrix):
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

def fill(grid, matrix):

	# water in four corners
    matrix.place(info.water_length, info.water_width, 0, 0, "~")
    matrix.place(info.water_length, info.water_width, info.grid_length-info.water_length, 0, "~")
    matrix.place(info.water_length, info.water_width, 0, info.grid_width-info.water_width, "~")
    matrix.place(info.water_length, info.water_width, info.grid_length-info.water_length, info.grid_width-info.water_width, "~")

    # # water in two corners
    # matrix.place(int(info.water_length / 2), info.water_width * 2, 0, 0, "~")
    # matrix.place(int(info.water_length * 1.5), int(info.water_width / 1.5), int(info.water_length / 2), 0, "~")
    # matrix.place(int(info.water_length / 2), info.water_width * 2, info.grid_length-int(info.water_length / 2), info.grid_width-info.water_width * 2, "~")
    # matrix.place(int(info.water_length * 1.5), int(info.water_width / 1.5), info.grid_length - int(info.water_length * 1.5) - int(info.water_length / 2), info.grid_width-int(info.water_length / 1.5), "~")
    
    start_x = int(info.grid_length * 0.5)
    start_y = int(info.grid_width * 0.5)

    houses_at_start = []

    houses_at_start_2 = []

    factor_x = start_x

    factor_y = start_y

    check = matrix.check(info.house_m_length, info.house_m_width, info.house_m_free, factor_x, factor_y)
    if check == 0:
        print("check 1!")
        hd.houses_m[hd.house_m_counter] = House(info.house_m_type, ("M{0:02}".format(hd.house_m_counter)), info.house_m_free, info.house_m_value, factor_x, factor_y, info.house_m_length, info.house_m_width)
        matrix.place(info.house_m_length, info.house_m_width, factor_x, factor_y, hd.houses_m[hd.house_m_counter].id)

        print("success {}".format(hd.houses_m[hd.house_m_counter].id))

        houses_at_start.append(hd.houses_m[hd.house_m_counter])
        hd.house_m_counter = hd.house_m_counter + 1

    while (hd.house_e_counter - 1 + hd.house_b_counter - 1 + hd.house_m_counter - 1) < info.number_of_houses:

        factor_x = int(factor_x * 0.5)
        factor_y = int(factor_y * 0.5)

        for q in houses_at_start:

            if (hd.house_e_counter - 1 + hd.house_b_counter - 1 + hd.house_m_counter - 1) < info.number_of_houses:

                if hd.house_m_counter <= info.house_m_number:

                    check = matrix.check(info.house_m_length, info.house_m_width, info.house_m_free, q.xcor - factor_x, q.ycor - factor_y)
                    if check == 0:
                        hd.houses_m[hd.house_m_counter] = House(info.house_m_type, ("M{0:02}".format(hd.house_m_counter)), info.house_m_free, info.house_m_value, q.xcor - factor_x, q.ycor - factor_y, info.house_m_length, info.house_m_width)
                        matrix.place(info.house_m_length, info.house_m_width, q.xcor - factor_x, q.ycor - factor_y, hd.houses_m[hd.house_m_counter].id)

                        print("success {}".format(hd.houses_m[hd.house_m_counter].id))

                        houses_at_start_2.append(hd.houses_m[hd.house_m_counter])
                        hd.house_m_counter = hd.house_m_counter + 1

                elif hd.house_b_counter <= info.house_b_number:

                    check = matrix.check(info.house_b_length, info.house_b_width, info.house_b_free, q.xcor - factor_x, q.ycor - factor_y)
                    if check == 0:
                        hd.houses_b[hd.house_b_counter] = House(info.house_b_type, ("B{0:02}".format(hd.house_b_counter)), info.house_b_free, info.house_b_value, q.xcor - factor_x, q.ycor - factor_y, info.house_b_length, info.house_b_width)
                        matrix.place(info.house_b_length, info.house_b_width, q.xcor - factor_x, q.ycor - factor_y, hd.houses_b[hd.house_b_counter].id)

                        print("success {}".format(hd.houses_b[hd.house_b_counter].id))

                        houses_at_start_2.append(hd.houses_b[hd.house_b_counter])
                        hd.house_b_counter = hd.house_b_counter + 1

                elif hd.house_e_counter <= info.house_e_number:

                    check = matrix.check(info.house_e_length, info.house_e_width, info.house_e_free, q.xcor - factor_x, q.ycor - factor_y)
                    if check == 0:
                        hd.houses_e[hd.house_e_counter] = House(info.house_e_type, ("E{0:02}".format(hd.house_e_counter)), info.house_e_free, info.house_e_value, q.xcor - factor_x, q.ycor - factor_y, info.house_e_length, info.house_e_width)
                        matrix.place(info.house_e_length, info.house_e_width, q.xcor - factor_x, q.ycor - factor_y, hd.houses_e[hd.house_e_counter].id)

                        print("success {}".format(hd.houses_e[hd.house_e_counter].id))

                        houses_at_start_2.append(hd.houses_e[hd.house_e_counter])
                        hd.house_e_counter = hd.house_e_counter + 1

            if (hd.house_e_counter - 1 + hd.house_b_counter - 1 + hd.house_m_counter - 1) < info.number_of_houses:

                if hd.house_m_counter <= info.house_m_number:

                    check = matrix.check(info.house_m_length, info.house_m_width, info.house_m_free, q.xcor - factor_x, q.ycor + factor_y)
                    if check == 0:
                        hd.houses_m[hd.house_m_counter] = House(info.house_m_type, ("M{0:02}".format(hd.house_m_counter)), info.house_m_free, info.house_m_value, q.xcor - factor_x, q.ycor + factor_y, info.house_m_length, info.house_m_width)
                        matrix.place(info.house_m_length, info.house_m_width, q.xcor - factor_x, q.ycor + factor_y, hd.houses_m[hd.house_m_counter].id)

                        print("success {}".format(hd.houses_m[hd.house_m_counter].id))

                        houses_at_start_2.append(hd.houses_m[hd.house_m_counter])
                        hd.house_m_counter = hd.house_m_counter + 1

                elif hd.house_b_counter <= info.house_b_number:

                    check = matrix.check(info.house_b_length, info.house_b_width, info.house_b_free, q.xcor - factor_x, q.ycor + factor_y)
                    if check == 0:
                        hd.houses_b[hd.house_b_counter] = House(info.house_b_type, ("B{0:02}".format(hd.house_b_counter)), info.house_b_free, info.house_b_value, q.xcor - factor_x, q.ycor + factor_y, info.house_b_length, info.house_b_width)
                        matrix.place(info.house_b_length, info.house_b_width, q.xcor - factor_x, q.ycor + factor_y, hd.houses_b[hd.house_b_counter].id)

                        print("success {}".format(hd.houses_b[hd.house_b_counter].id))

                        houses_at_start_2.append(hd.houses_b[hd.house_b_counter])
                        hd.house_b_counter = hd.house_b_counter + 1

                elif hd.house_e_counter <= info.house_e_number:

                    check = matrix.check(info.house_e_length, info.house_e_width, info.house_e_free, q.xcor - factor_x, q.ycor + factor_y)
                    if check == 0:
                        hd.houses_e[hd.house_e_counter] = House(info.house_e_type, ("E{0:02}".format(hd.house_e_counter)), info.house_e_free, info.house_e_value, q.xcor - factor_x, q.ycor + factor_y, info.house_e_length, info.house_e_width)
                        matrix.place(info.house_e_length, info.house_e_width, q.xcor - factor_x, q.ycor + factor_y, hd.houses_e[hd.house_e_counter].id)

                        print("success {}".format(hd.houses_e[hd.house_e_counter].id))

                        houses_at_start_2.append(hd.houses_e[hd.house_e_counter])
                        hd.house_e_counter = hd.house_e_counter + 1

            if (hd.house_e_counter - 1 + hd.house_b_counter - 1 + hd.house_m_counter - 1) < info.number_of_houses:

                if hd.house_m_counter <= info.house_m_number:

                    check = matrix.check(info.house_m_length, info.house_m_width, info.house_m_free, q.xcor + factor_x, q.ycor - factor_y)
                    if check == 0:
                        hd.houses_m[hd.house_m_counter] = House(info.house_m_type, ("M{0:02}".format(hd.house_m_counter)), info.house_m_free, info.house_m_value, q.xcor + factor_x, q.ycor - factor_y, info.house_m_length, info.house_m_width)
                        matrix.place(info.house_m_length, info.house_m_width, q.xcor + factor_x, q.ycor - factor_y, hd.houses_m[hd.house_m_counter].id)

                        print("success {}".format(hd.houses_m[hd.house_m_counter].id))

                        houses_at_start_2.append(hd.houses_m[hd.house_m_counter])
                        hd.house_m_counter = hd.house_m_counter + 1

                elif hd.house_b_counter <= info.house_b_number:

                    check = matrix.check(info.house_b_length, info.house_b_width, info.house_b_free, q.xcor + factor_x, q.ycor - factor_y)
                    if check == 0:
                        hd.houses_b[hd.house_b_counter] = House(info.house_b_type, ("B{0:02}".format(hd.house_b_counter)), info.house_b_free, info.house_b_value, q.xcor + factor_x, q.ycor - factor_y, info.house_b_length, info.house_b_width)
                        matrix.place(info.house_b_length, info.house_b_width, q.xcor + factor_x, q.ycor - factor_y, hd.houses_b[hd.house_b_counter].id)

                        print("success {}".format(hd.houses_b[hd.house_b_counter].id))

                        houses_at_start_2.append(hd.houses_b[hd.house_b_counter])
                        hd.house_b_counter = hd.house_b_counter + 1

                elif hd.house_e_counter <= info.house_e_number:

                    check = matrix.check(info.house_e_length, info.house_e_width, info.house_e_free, q.xcor + factor_x, q.ycor - factor_y)
                    if check == 0:
                        hd.houses_e[hd.house_e_counter] = House(info.house_e_type, ("E{0:02}".format(hd.house_e_counter)), info.house_e_free, info.house_e_value, q.xcor + factor_x, q.ycor - factor_y, info.house_e_length, info.house_e_width)
                        matrix.place(info.house_e_length, info.house_e_width, q.xcor + factor_x, q.ycor - factor_y, hd.houses_e[hd.house_e_counter].id)

                        print("success {}".format(hd.houses_e[hd.house_e_counter].id))

                        houses_at_start_2.append(hd.houses_e[hd.house_e_counter])
                        hd.house_e_counter = hd.house_e_counter + 1


            if (hd.house_e_counter - 1 + hd.house_b_counter - 1 + hd.house_m_counter - 1) < info.number_of_houses:

                if hd.house_m_counter <= info.house_m_number:

                    check = matrix.check(info.house_m_length, info.house_m_width, info.house_m_free, q.xcor + factor_x, q.ycor + factor_y)
                    if check == 0:
                        hd.houses_m[hd.house_m_counter] = House(info.house_m_type, ("M{0:02}".format(hd.house_m_counter)), info.house_m_free, info.house_m_value, q.xcor + factor_x, q.ycor + factor_y, info.house_m_length, info.house_m_width)
                        matrix.place(info.house_m_length, info.house_m_width, q.xcor + factor_x, q.ycor + factor_y, hd.houses_m[hd.house_m_counter].id)

                        print("success {}".format(hd.houses_m[hd.house_m_counter].id))

                        houses_at_start_2.append(hd.houses_m[hd.house_m_counter])
                        hd.house_m_counter = hd.house_m_counter + 1

                elif hd.house_b_counter <= info.house_b_number:

                    check = matrix.check(info.house_b_length, info.house_b_width, info.house_b_free, q.xcor + factor_x, q.ycor + factor_y)
                    if check == 0:
                        hd.houses_b[hd.house_b_counter] = House(info.house_b_type, ("B{0:02}".format(hd.house_b_counter)), info.house_b_free, info.house_b_value, q.xcor + factor_x, q.ycor + factor_y, info.house_b_length, info.house_b_width)
                        matrix.place(info.house_b_length, info.house_b_width, q.xcor + factor_x, q.ycor + factor_y, hd.houses_b[hd.house_b_counter].id)

                        print("success {}".format(hd.houses_b[hd.house_b_counter].id))

                        houses_at_start_2.append(hd.houses_b[hd.house_b_counter])
                        hd.house_b_counter = hd.house_b_counter + 1

                elif hd.house_e_counter <= info.house_e_number:

                    check = matrix.check(info.house_e_length, info.house_e_width, info.house_e_free, q.xcor + factor_x, q.ycor + factor_y)
                    if check == 0:
                        hd.houses_e[hd.house_e_counter] = House(info.house_e_type, ("E{0:02}".format(hd.house_e_counter)), info.house_e_free, info.house_e_value, q.xcor + factor_x, q.ycor + factor_y, info.house_e_length, info.house_e_width)
                        matrix.place(info.house_e_length, info.house_e_width, q.xcor + factor_x, q.ycor + factor_y, hd.houses_e[hd.house_e_counter].id)

                        print("success {}".format(hd.houses_e[hd.house_e_counter].id))

                        houses_at_start_2.append(hd.houses_e[hd.house_e_counter])
                        hd.house_e_counter = hd.house_e_counter + 1

        houses_at_start = houses_at_start_2



    #         matrix.place(info.house_e_length, info.house_e_width, best_x_cor, best_y_cor, hd.houses_e[hd.house_e_counter].id)
    #         hd.house_e_counter+=1
    #         print("success {}".format(hd.houses_e[hd.house_e_counter].id))
