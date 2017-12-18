import library.house_dictionary as hd
import library.setup as info

def calculate_all():

    # calculate free space of all available houses
    calculate_houses('houses_e')
    calculate_houses('houses_b')
    calculate_houses('houses_m')

def calculate_houses(type):

    houses_t = getattr(hd, type)

    # iterate through all houses in dictinary
    for house in houses_t:
        lowest_c = info.grid_width
        # distance to top x-axis
        c_top = abs(houses_t[house].xcor - 0)
        # distance to bottom x-axis
        c_bottom = abs(houses_t[house].xcor - info.grid_width)
        # = distance to left y-axis
        c_left = abs(houses_t[house].ycor - 0)
        # distance to right y-axis
        c_right = abs(houses_t[house].ycor - info.grid_length)

        lowest_c = min(c_top, c_bottom, c_left, c_right)

        # find smallest distance between house and other houses in y-axis
        for x in range(houses_t[house].xcor, houses_t[house].xcor + houses_t[house].length):
            for i in hd.houses_e:
                if(houses_t[house].id == hd.houses_e[i].id):
                    continue
                    #next(hd.houses_e)

                for j in range(hd.houses_e[i].xcor, hd.houses_e[i].xcor + hd.houses_e[i].length):
                    if (x == j):
                        for y in range(houses_t[house].ycor, houses_t[house].ycor + houses_t[house].width):
                            for k in range(hd.houses_e[i].ycor, hd.houses_e[i].ycor + hd.houses_e[i].width):
                                if(abs(y-k) < lowest_c):
                                    lowest_c = abs(y-k)

        # find smallest distance between house and other bungalow houses in y-axis
            for i in hd.houses_b:
                if(houses_t[house].id == hd.houses_b[i].id):
                    continue
                for j in range(hd.houses_b[i].xcor, hd.houses_b[i].xcor + hd.houses_b[i].length):
                    if (x == j):
                        for y in range(houses_t[house].ycor, houses_t[house].ycor + houses_t[house].width):
                            for k in range(hd.houses_b[i].ycor, hd.houses_b[i].ycor + hd.houses_b[i].width):
                                if(abs(y-k) < lowest_c):
                                    lowest_c = abs(y-k)

        # find smallest distance between house and other maison houses in y-axis
            for i in hd.houses_m:
                if(houses_t[house].id == hd.houses_m[i].id):
                    continue
                for j in range(hd.houses_m[i].xcor, hd.houses_m[i].xcor + hd.houses_m[i].length):
                    if (x == j):
                        for y in range(houses_t[house].ycor, houses_t[house].ycor + houses_t[house].width):
                            for k in range(hd.houses_m[i].ycor, hd.houses_m[i].ycor + hd.houses_m[i].width):
                                if(abs(y-k) < lowest_c):
                                    lowest_c = abs(y-k)

        # find smallest distance between house and other houses in x-axis
        for y in range(houses_t[house].ycor, houses_t[house].ycor + houses_t[house].width):
            for i in hd.houses_e:
                if(houses_t[house].id == hd.houses_e[i].id):
                    continue
                for j in range(hd.houses_e[i].ycor, hd.houses_e[i].ycor + hd.houses_e[i].width):
                    if (y == j):
                        for x in range(houses_t[house].xcor, houses_t[house].xcor + houses_t[house].length):
                            for k in range(hd.houses_e[i].xcor, hd.houses_e[i].xcor + hd.houses_e[i].length):
                                if(abs(x-k) < lowest_c):
                                    lowest_c = abs(x-k)

            for i in hd.houses_b:
                if(houses_t[house].id == hd.houses_b[i].id):
                    continue
                for j in range(hd.houses_b[i].ycor, hd.houses_b[i].ycor + hd.houses_b[i].width):
                    if (y == j):
                        for x in range(houses_t[house].xcor, houses_t[house].xcor + houses_t[house].length):
                            for k in range(hd.houses_b[i].xcor, hd.houses_b[i].xcor + hd.houses_b[i].length):
                                if(abs(x-k) < lowest_c):
                                    lowest_c = abs(x-k)

            for i in hd.houses_m:
                if(houses_t[house].id == hd.houses_m[i].id):
                    continue
                for j in range(hd.houses_m[i].ycor, hd.houses_m[i].ycor + hd.houses_m[i].width):
                    if (y == j):
                        for x in range(houses_t[house].xcor, houses_t[house].xcor + houses_t[house].length):
                            for k in range(hd.houses_m[i].xcor, hd.houses_m[i].xcor + hd.houses_m[i].length):
                                if(abs(x-k) < lowest_c):
                                    lowest_c = abs(x-k)

        # find smallest distance between house and other houses in diagonal
        for i in hd.houses_e:
            if(houses_t[house].id == hd.houses_e[i].id):
                continue
            a = houses_t[house].xcor - (hd.houses_e[i].xcor + hd.houses_e[i].length)
            b = houses_t[house].ycor - (hd.houses_e[i].ycor + hd.houses_e[i].width)
            c = (a**2 + b**2)**0.5
            if(c < lowest_c):
                lowest_c = c

            a = houses_t[house].xcor - (hd.houses_e[i].xcor + hd.houses_e[i].length)
            b = (houses_t[house].ycor + houses_t[house].width) - hd.houses_e[i].ycor
            c = (a**2 + b**2)**0.5
            if(c < lowest_c):
                lowest_c = c

            a = (houses_t[house].xcor + houses_t[house].length) - hd.houses_e[i].xcor
            b = houses_t[house].ycor - (hd.houses_e[i].ycor + hd.houses_e[i].width)
            c = (a**2 + b**2)**0.5
            if(c < lowest_c):
                lowest_c = c

            a = (houses_t[house].xcor + houses_t[house].length) - hd.houses_e[i].xcor
            b = (houses_t[house].ycor + houses_t[house].width) - hd.houses_e[i].ycor
            c = (a**2 + b**2)**0.5
            if(c < lowest_c):
                lowest_c = c

        # find smallest distance between house and other houses in diagonal
        for i in hd.houses_b:
            if(houses_t[house].id == hd.houses_b[i].id):
                continue
            a = houses_t[house].xcor - (hd.houses_b[i].xcor + hd.houses_b[i].length)
            b = houses_t[house].ycor - (hd.houses_b[i].ycor + hd.houses_b[i].width)
            c = (a**2 + b**2)**0.5
            if(c < lowest_c):
                lowest_c = c

            a = houses_t[house].xcor - (hd.houses_b[i].xcor + hd.houses_b[i].length)
            b = (houses_t[house].ycor + houses_t[house].width) - hd.houses_b[i].ycor
            c = (a**2 + b**2)**0.5
            if(c < lowest_c):
                lowest_c = c

            a = (houses_t[house].xcor + houses_t[house].length) - hd.houses_b[i].xcor
            b = houses_t[house].ycor - (hd.houses_b[i].ycor + hd.houses_b[i].width)
            c = (a**2 + b**2)**0.5
            if(c < lowest_c):
                lowest_c = c

            a = (houses_t[house].xcor + houses_t[house].length) - hd.houses_b[i].xcor
            b = (houses_t[house].ycor + houses_t[house].width) - hd.houses_b[i].ycor
            c = (a**2 + b**2)**0.5
            if(c < lowest_c):
                lowest_c = c

        # find smallest distance between house and other houses in diagonal
        for i in hd.houses_m:
            if(houses_t[house].id == hd.houses_m[i].id):
                continue
            a = houses_t[house].xcor - (hd.houses_m[i].xcor + hd.houses_m[i].length)
            b = houses_t[house].ycor - (hd.houses_m[i].ycor + hd.houses_m[i].width)
            c = (a**2 + b**2)**0.5
            if(c < lowest_c):
                lowest_c = c

            a = houses_t[house].xcor - (hd.houses_m[i].xcor + hd.houses_m[i].length)
            b = (houses_t[house].ycor + houses_t[house].width) - hd.houses_m[i].ycor
            c = (a**2 + b**2)**0.5
            if(c < lowest_c):
                lowest_c = c

            a = (houses_t[house].xcor + houses_t[house].length) - hd.houses_m[i].xcor
            b = houses_t[house].ycor - (hd.houses_m[i].ycor + hd.houses_m[i].width)
            c = (a**2 + b**2)**0.5
            if(c < lowest_c):
                lowest_c = c

            a = (houses_t[house].xcor + houses_t[house].length) - hd.houses_m[i].xcor
            b = (houses_t[house].ycor + houses_t[house].width) - hd.houses_m[i].ycor
            c = (a**2 + b**2)**0.5
            if(c < lowest_c):
                lowest_c = c

        houses_t[house].free = lowest_c
