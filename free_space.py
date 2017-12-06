import house_dictionary as hd
import setup as info

def calculate_free_space():

    # iterate through all houses in dictinary
    for house in hd.houses_e:
        lowest_c = info.grid_width

        # find smallest distance between house and other houses in y-axis
        for x in range(house.xcor, house.xcor + house.length):
            for i in hd.houses_e:
                if(house.id == i.id):
                    continue
                    # next(hd.houses_e)
                for j in range(i.xcor, i.xcor + i.length):
                    if (x == j):
                        for y in range(house.ycor, house.ycor + house.width):
                            for k in range(i.ycor, i.ycor + i.width):
                                if(abs(y-k) < lowest_c):
                                    lowest_c = abs(y-k)

        # find smallest distance between house and other houses in x-axis
        for y in range(house.ycor, house.ycor + house.width):
            for i in hd.houses_e:
                if(house.id == i.id):
                    continue
                for j in range(i.ycor, i.ycor + i.width):
                    if (y == j):
                        for x in range(house.xcor, house.xcor + house.length):
                            for k in range(i.xcor, i.xcor + i.length):
                                if(abs(x-k) < lowest_c):
                                    lowest_c = abs(x-k)


        # find smallest distance between house and other houses in diagonal
        for i in hd.houses_e:
            a = house.xcor - (i.xcor + i.length)
            b = house.ycor - (i.ycor + i.width)
            c = (a**2 + b**2)**0.5
            if(c < lowest_c):
                lowest_c = c

            a = house.xcor - (i.xcor + i.length)
            b = (house.ycor + house.width) - i.ycor
            c = (a**2 + b**2)**0.5
            if(c < lowest_c):
                lowest_c = c

            a = (house.xcor + house.length) - i.xcor
            b = house.ycor - (i.ycor + i.width)
            c = (a**2 + b**2)**0.5
            if(c < lowest_c):
                lowest_c = c

            a = (house.xcor + house.length) - i.xcor
            b = (house.ycor + house.width) - i.ycor
            c = (a**2 + b**2)**0.5
            if(c < lowest_c):
                lowest_c = c

        house.free = lowest_c
