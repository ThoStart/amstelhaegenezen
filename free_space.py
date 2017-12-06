import house_dictionary as hd
import setup as info

def calculate_free_space():

    # iterate through all houses in dictinary
    for house in hd.houses_e:
        lowest_c = info.grid_width
        # distance to top x-axis
        c_top = abs(hd.houses_e[house].xcor - 0)
        # distance to bottom x-axis
        c_bottom = abs(hd.houses_e[house].xcor - info.grid_width)
        # = distance to left y-axis
        c_left = abs(hd.houses_e[house].ycor - 0)
        # distance to right y-axis
        c_right = abs(hd.houses_e[house].ycor - info.grid_length)

        lowest_c = min(c_top, c_bottom, c_left, c_right)


        # find smallest distance between house and other houses in y-axis
        for x in range(hd.houses_e[house].xcor, hd.houses_e[house].xcor + hd.houses_e[house].length):
            for i in hd.houses_e:
                if(hd.houses_e[house].id == hd.houses_e[i].id):
                    continue
                    #next(hd.houses_e)
            #    else:

                for j in range(hd.houses_e[i].xcor, hd.houses_e[i].xcor + hd.houses_e[i].length):
                    if (x == j):
                        for y in range(hd.houses_e[house].ycor, hd.houses_e[house].ycor + hd.houses_e[house].width):
                            for k in range(hd.houses_e[i].ycor, hd.houses_e[i].ycor + hd.houses_e[i].width):
                                if(abs(y-k) < lowest_c):
                                    lowest_c = abs(y-k)

        # find smallest distance between house and other houses in x-axis
        for y in range(hd.houses_e[house].ycor, hd.houses_e[house].ycor + hd.houses_e[house].width):
            for i in hd.houses_e:
                if(hd.houses_e[house].id == hd.houses_e[i].id):
                    continue
                for j in range(hd.houses_e[i].ycor, hd.houses_e[i].ycor + hd.houses_e[i].width):
                    if (y == j):
                        for x in range(hd.houses_e[house].xcor, hd.houses_e[house].xcor + hd.houses_e[house].length):
                            for k in range(hd.houses_e[i].xcor, hd.houses_e[i].xcor + hd.houses_e[i].length):
                                if(abs(x-k) < lowest_c):
                                    lowest_c = abs(x-k)


        # find smallest distance between house and other houses in diagonal
        for i in hd.houses_e:
            if(hd.houses_e[house].id == hd.houses_e[i].id):
                continue
            a = hd.houses_e[house].xcor - (hd.houses_e[i].xcor + hd.houses_e[i].length)
            b = hd.houses_e[house].ycor - (hd.houses_e[i].ycor + hd.houses_e[i].width)
            c = (a**2 + b**2)**0.5
            if(c < lowest_c):
                lowest_c = c

            a = hd.houses_e[house].xcor - (hd.houses_e[i].xcor + hd.houses_e[i].length)
            b = (hd.houses_e[house].ycor + hd.houses_e[house].width) - hd.houses_e[i].ycor
            c = (a**2 + b**2)**0.5
            if(c < lowest_c):
                lowest_c = c

            a = (hd.houses_e[house].xcor + hd.houses_e[house].length) - hd.houses_e[i].xcor
            b = hd.houses_e[house].ycor - (hd.houses_e[i].ycor + hd.houses_e[i].width)
            c = (a**2 + b**2)**0.5
            if(c < lowest_c):
                lowest_c = c

            a = (hd.houses_e[house].xcor + hd.houses_e[house].length) - hd.houses_e[i].xcor
            b = (hd.houses_e[house].ycor + hd.houses_e[house].width) - hd.houses_e[i].ycor
            c = (a**2 + b**2)**0.5
            if(c < lowest_c):
                lowest_c = c

        hd.houses_e[house].free = lowest_c
        print(lowest_c)
