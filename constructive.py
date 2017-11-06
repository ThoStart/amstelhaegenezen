#!/usr/bin/env python3

from class_objects import *

empty = '.'
vrij = 'v'

#unused
def readground(cx,cy):
    for y in range(int(house_m.length) + 2):
        for x in range(house_m.width + 2):
            if (cursor_x + x) >= ground.width - 1:
                    cursor_x = 0
                    cursor_y = cursor_y + int(house_m.length) - y + 1
                    x = -1
                    y = -1               
            elif ground.grid[cursor_y + y][cursor_x + x] != empty and vrij:
                cursor_x = cursor_x + x
                x = -1
                y = 0 


for y in range(ground.length):
    ground.grid.append([])
    for x in range(ground.width): 
        ground.grid[y].append(empty)  

numbers = []
g = 0
numbers.append([])
for i in range(ground.width):
    numbers[0].append(g)
    g = g + 1
    if g == 10:
        g = 0

cursor_x = 0
cursor_y = 0

# hard-coded
for n in range(2):
    huizen = [12,5,3]
    while True:
        for y in range(int(house_m.length) + 2):
            for x in range(house_m.width + 2):
                if (cursor_x + x) >= ground.width - 1:
                    cursor_x = 0
                    cursor_y = cursor_y + int(house_m.length) - y + 1
                    x = 0
                    y = 0               
                elif ground.grid[cursor_y + y][cursor_x + x] != empty:
                    cursor_x = cursor_x + x
                    x = 0
                    y = 0
        for y in range(int(house_m.length)+2):
            for x in range(house_m.width+2):
                ground.grid[cursor_y + y][cursor_x + x] = vrij                                         
        for y in range(int(house_m.length)):
            for x in range(house_m.width):
                ground.grid[cursor_y + y + 1][cursor_x + x + 1] = 'M'
        huizen[2] = huizen[2] - 1
        if huizen[2] == 0:
            break

    while True:
        for y in range(int(house_m.length) + 2):
            for x in range(house_m.width + 2):
                if (cursor_x + x) >= ground.width - 1:
                    cursor_x = 0
                    cursor_y = cursor_y + int(house_b.length) - y + 1
                    x = 0
                    y = 0           
                elif ground.grid[cursor_y + y][cursor_x + x] != empty:
                    cursor_x = cursor_x + x
                    x = 0
                    y = 0
            #cursor_y = cursor_y + 1
        for y in range(int(house_b.length)+2):
            for x in range(house_b.width+2):
                ground.grid[cursor_y + y][cursor_x + x] = vrij                                         
        for y in range(int(house_b.length)):
            for x in range(house_b.width):
                ground.grid[cursor_y + y + 1][cursor_x + x + 1] = 'B'
        huizen[1] = huizen[1] - 1
        if huizen[1] == 0:
            break

    while True:
        for y in range(int(house_m.length) + 2):
            for x in range(house_m.width + 2):
                if (cursor_x + x) >= ground.width - 1:
                    #print("X: ", end="")
                    #print(cursor_x, end=", ")
                    #print(ground.grid[y][x])
                    cursor_x = 0
                    cursor_y = cursor_y + house_e.length - y + 1
                    x = 0
                    y = 0      
                elif ground.grid[cursor_y + y][cursor_x + x] != empty:
                    cursor_x = cursor_x + 1
                    x = 0
                    y = 0
                    #if x == house_m.width + 2: 
                    #    cursor_y = cursor_y +1
        #print(cursor_x, end="")
        #print(", ", end="")
        #print(cursor_y)
        for y in range(house_e.length+2):
            for x in range(house_e.width+2):
                ground.grid[cursor_y + y][cursor_x + x] = 'v'                                 
        for y in range(house_e.length):
            for x in range(house_e.width):
                ground.grid[cursor_y + y + 1][cursor_x + x + 1] = 'E'
        huizen[0] = huizen[0] - 1
        if huizen[0] == 0:
            break



# ff printen
print("grid width: {}, length: {}, E:B:W ratio: 12:5:3".format(ground.width, ground.length))

print(" ", end="")
for c in range(ground.width):
    print(numbers[0][c], end="")      
print()        
for i in range(ground.length):
    print(numbers[0][i], end="")
    for elt in ground.grid[i] :
        print("" + elt, end="")
    print()                         
