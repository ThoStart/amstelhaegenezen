from classes.class_objects import House, Water, Matrix
import library.setup as info
import library.house_dictionary as hd

def fill(grid, matrix):

    # declare variables
    start_x = int(info.grid_length * 0.5)
    start_y = int(info.grid_width * 0.5)
    houses_at_start = []
    houses_at_start_2 = []
    factor_x = start_x
    factor_y = start_y

    # find empty spot in center
    check = matrix.check(info.house_m_length, info.house_m_width, info.house_m_free, factor_x, factor_y)
    if check == 0:
        hd.houses_m[hd.house_m_counter] = House(info.house_m_type, ("M{0:02}".format(hd.house_m_counter)), info.house_m_free, info.house_m_value, factor_x, factor_y, info.house_m_length, info.house_m_width)
        matrix.place(info.house_m_length, info.house_m_width, factor_x, factor_y, hd.houses_m[hd.house_m_counter].id)

        houses_at_start.append(hd.houses_m[hd.house_m_counter])
        hd.house_m_counter = hd.house_m_counter + 1

    while (hd.house_e_counter - 1 + hd.house_b_counter - 1 + hd.house_m_counter - 1) < info.number_of_houses:

        # find center of each side of the previously placed house
        factor_x = int(factor_x * 0.5)
        factor_y = int(factor_y * 0.5)

        for q in houses_at_start:

            if (hd.house_e_counter - 1 + hd.house_b_counter - 1 + hd.house_m_counter - 1) < info.number_of_houses:

                # check and place exact number of maisons, bungalows and eengezinswoningen
                if hd.house_m_counter <= info.house_m_number:

                    check = matrix.check(info.house_m_length, info.house_m_width, info.house_m_free, q.xcor - factor_x, q.ycor - factor_y)
                    if check == 0:
                        hd.houses_m[hd.house_m_counter] = House(info.house_m_type, ("M{0:02}".format(hd.house_m_counter)), info.house_m_free, info.house_m_value, q.xcor - factor_x, q.ycor - factor_y, info.house_m_length, info.house_m_width)
                        matrix.place(info.house_m_length, info.house_m_width, q.xcor - factor_x, q.ycor - factor_y, hd.houses_m[hd.house_m_counter].id)

                        houses_at_start_2.append(hd.houses_m[hd.house_m_counter])
                        hd.house_m_counter = hd.house_m_counter + 1

                elif hd.house_b_counter <= info.house_b_number:

                    check = matrix.check(info.house_b_length, info.house_b_width, info.house_b_free, q.xcor - factor_x, q.ycor - factor_y)
                    if check == 0:
                        hd.houses_b[hd.house_b_counter] = House(info.house_b_type, ("B{0:02}".format(hd.house_b_counter)), info.house_b_free, info.house_b_value, q.xcor - factor_x, q.ycor - factor_y, info.house_b_length, info.house_b_width)
                        matrix.place(info.house_b_length, info.house_b_width, q.xcor - factor_x, q.ycor - factor_y, hd.houses_b[hd.house_b_counter].id)

                        houses_at_start_2.append(hd.houses_b[hd.house_b_counter])
                        hd.house_b_counter = hd.house_b_counter + 1

                elif hd.house_e_counter <= info.house_e_number:

                    check = matrix.check(info.house_e_length, info.house_e_width, info.house_e_free, q.xcor - factor_x, q.ycor - factor_y)
                    if check == 0:
                        hd.houses_e[hd.house_e_counter] = House(info.house_e_type, ("E{0:02}".format(hd.house_e_counter)), info.house_e_free, info.house_e_value, q.xcor - factor_x, q.ycor - factor_y, info.house_e_length, info.house_e_width)
                        matrix.place(info.house_e_length, info.house_e_width, q.xcor - factor_x, q.ycor - factor_y, hd.houses_e[hd.house_e_counter].id)

                        houses_at_start_2.append(hd.houses_e[hd.house_e_counter])
                        hd.house_e_counter = hd.house_e_counter + 1

            if (hd.house_e_counter - 1 + hd.house_b_counter - 1 + hd.house_m_counter - 1) < info.number_of_houses:

                if hd.house_m_counter <= info.house_m_number:

                    check = matrix.check(info.house_m_length, info.house_m_width, info.house_m_free, q.xcor - factor_x, q.ycor + factor_y)
                    if check == 0:
                        hd.houses_m[hd.house_m_counter] = House(info.house_m_type, ("M{0:02}".format(hd.house_m_counter)), info.house_m_free, info.house_m_value, q.xcor - factor_x, q.ycor + factor_y, info.house_m_length, info.house_m_width)
                        matrix.place(info.house_m_length, info.house_m_width, q.xcor - factor_x, q.ycor + factor_y, hd.houses_m[hd.house_m_counter].id)

                        houses_at_start_2.append(hd.houses_m[hd.house_m_counter])
                        hd.house_m_counter = hd.house_m_counter + 1

                elif hd.house_b_counter <= info.house_b_number:

                    check = matrix.check(info.house_b_length, info.house_b_width, info.house_b_free, q.xcor - factor_x, q.ycor + factor_y)
                    if check == 0:
                        hd.houses_b[hd.house_b_counter] = House(info.house_b_type, ("B{0:02}".format(hd.house_b_counter)), info.house_b_free, info.house_b_value, q.xcor - factor_x, q.ycor + factor_y, info.house_b_length, info.house_b_width)
                        matrix.place(info.house_b_length, info.house_b_width, q.xcor - factor_x, q.ycor + factor_y, hd.houses_b[hd.house_b_counter].id)

                        houses_at_start_2.append(hd.houses_b[hd.house_b_counter])
                        hd.house_b_counter = hd.house_b_counter + 1

                elif hd.house_e_counter <= info.house_e_number:

                    check = matrix.check(info.house_e_length, info.house_e_width, info.house_e_free, q.xcor - factor_x, q.ycor + factor_y)
                    if check == 0:
                        hd.houses_e[hd.house_e_counter] = House(info.house_e_type, ("E{0:02}".format(hd.house_e_counter)), info.house_e_free, info.house_e_value, q.xcor - factor_x, q.ycor + factor_y, info.house_e_length, info.house_e_width)
                        matrix.place(info.house_e_length, info.house_e_width, q.xcor - factor_x, q.ycor + factor_y, hd.houses_e[hd.house_e_counter].id)

                        houses_at_start_2.append(hd.houses_e[hd.house_e_counter])
                        hd.house_e_counter = hd.house_e_counter + 1

            if (hd.house_e_counter - 1 + hd.house_b_counter - 1 + hd.house_m_counter - 1) < info.number_of_houses:

                if hd.house_m_counter <= info.house_m_number:

                    check = matrix.check(info.house_m_length, info.house_m_width, info.house_m_free, q.xcor + factor_x, q.ycor - factor_y)
                    if check == 0:
                        hd.houses_m[hd.house_m_counter] = House(info.house_m_type, ("M{0:02}".format(hd.house_m_counter)), info.house_m_free, info.house_m_value, q.xcor + factor_x, q.ycor - factor_y, info.house_m_length, info.house_m_width)
                        matrix.place(info.house_m_length, info.house_m_width, q.xcor + factor_x, q.ycor - factor_y, hd.houses_m[hd.house_m_counter].id)

                        houses_at_start_2.append(hd.houses_m[hd.house_m_counter])
                        hd.house_m_counter = hd.house_m_counter + 1

                elif hd.house_b_counter <= info.house_b_number:

                    check = matrix.check(info.house_b_length, info.house_b_width, info.house_b_free, q.xcor + factor_x, q.ycor - factor_y)
                    if check == 0:
                        hd.houses_b[hd.house_b_counter] = House(info.house_b_type, ("B{0:02}".format(hd.house_b_counter)), info.house_b_free, info.house_b_value, q.xcor + factor_x, q.ycor - factor_y, info.house_b_length, info.house_b_width)
                        matrix.place(info.house_b_length, info.house_b_width, q.xcor + factor_x, q.ycor - factor_y, hd.houses_b[hd.house_b_counter].id)

                        houses_at_start_2.append(hd.houses_b[hd.house_b_counter])
                        hd.house_b_counter = hd.house_b_counter + 1

                elif hd.house_e_counter <= info.house_e_number:

                    check = matrix.check(info.house_e_length, info.house_e_width, info.house_e_free, q.xcor + factor_x, q.ycor - factor_y)
                    if check == 0:
                        hd.houses_e[hd.house_e_counter] = House(info.house_e_type, ("E{0:02}".format(hd.house_e_counter)), info.house_e_free, info.house_e_value, q.xcor + factor_x, q.ycor - factor_y, info.house_e_length, info.house_e_width)
                        matrix.place(info.house_e_length, info.house_e_width, q.xcor + factor_x, q.ycor - factor_y, hd.houses_e[hd.house_e_counter].id)

                        houses_at_start_2.append(hd.houses_e[hd.house_e_counter])
                        hd.house_e_counter = hd.house_e_counter + 1


            if (hd.house_e_counter - 1 + hd.house_b_counter - 1 + hd.house_m_counter - 1) < info.number_of_houses:

                if hd.house_m_counter <= info.house_m_number:

                    check = matrix.check(info.house_m_length, info.house_m_width, info.house_m_free, q.xcor + factor_x, q.ycor + factor_y)
                    if check == 0:
                        hd.houses_m[hd.house_m_counter] = House(info.house_m_type, ("M{0:02}".format(hd.house_m_counter)), info.house_m_free, info.house_m_value, q.xcor + factor_x, q.ycor + factor_y, info.house_m_length, info.house_m_width)
                        matrix.place(info.house_m_length, info.house_m_width, q.xcor + factor_x, q.ycor + factor_y, hd.houses_m[hd.house_m_counter].id)

                        houses_at_start_2.append(hd.houses_m[hd.house_m_counter])
                        hd.house_m_counter = hd.house_m_counter + 1

                elif hd.house_b_counter <= info.house_b_number:

                    check = matrix.check(info.house_b_length, info.house_b_width, info.house_b_free, q.xcor + factor_x, q.ycor + factor_y)
                    if check == 0:
                        hd.houses_b[hd.house_b_counter] = House(info.house_b_type, ("B{0:02}".format(hd.house_b_counter)), info.house_b_free, info.house_b_value, q.xcor + factor_x, q.ycor + factor_y, info.house_b_length, info.house_b_width)
                        matrix.place(info.house_b_length, info.house_b_width, q.xcor + factor_x, q.ycor + factor_y, hd.houses_b[hd.house_b_counter].id)

                        houses_at_start_2.append(hd.houses_b[hd.house_b_counter])
                        hd.house_b_counter = hd.house_b_counter + 1

                elif hd.house_e_counter <= info.house_e_number:

                    check = matrix.check(info.house_e_length, info.house_e_width, info.house_e_free, q.xcor + factor_x, q.ycor + factor_y)
                    if check == 0:
                        hd.houses_e[hd.house_e_counter] = House(info.house_e_type, ("E{0:02}".format(hd.house_e_counter)), info.house_e_free, info.house_e_value, q.xcor + factor_x, q.ycor + factor_y, info.house_e_length, info.house_e_width)
                        matrix.place(info.house_e_length, info.house_e_width, q.xcor + factor_x, q.ycor + factor_y, hd.houses_e[hd.house_e_counter].id)

                        houses_at_start_2.append(hd.houses_e[hd.house_e_counter])
                        hd.house_e_counter = hd.house_e_counter + 1

        houses_at_start = houses_at_start_2
