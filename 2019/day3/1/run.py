import math
import csv

with open('day3/1/input.csv', 'r') as input:
    reader = csv.reader(input)
    wireDirections = list(reader)

wire1Directions = wireDirections[0]
wire2Directions = wireDirections[1]

wire1Path = []
wire2Path = []
wire1PathFinal = []
wire2PathFinal = []

p0x = 0
p0y = 0

wire1Path.append(p0x)
wire1Path.append(p0y)
wire2Path.append(p0x)
wire2Path.append(p0y)
wire1PathFinal.append(str(p0x) + "," + str(p0y))


i = 0
while i < len(wire1Directions):
    direction = wire1Directions[i][0]
    length = wire1Directions[i][1:]

    if direction == "R":
        # right
        step = 1
        while step <= int(length):
            wire1Nowx = len(wire1Path) - 2
            wire1Nowy = len(wire1Path) - 1

            wire1Stepx = wire1Path[wire1Nowx] + 1
            wire1Stepy = wire1Path[wire1Nowy]

            wire1Path.append(wire1Stepx)
            wire1Path.append(wire1Stepy)
            wire1PathFinal.append(str(wire1Stepx) + "," + str(wire1Stepy))

            step += 1
    elif direction == "L":
        # left
        step = 1
        while step <= int(length):
            wire1Nowx = len(wire1Path) - 2
            wire1Nowy = len(wire1Path) - 1

            wire1Stepx = wire1Path[wire1Nowx] - 1
            wire1Stepy = wire1Path[wire1Nowy]

            wire1Path.append(wire1Stepx)
            wire1Path.append(wire1Stepy)
            wire1PathFinal.append(str(wire1Stepx) + "," + str(wire1Stepy))

            step += 1
    elif direction == "U":
        # up
        step = 1
        while step <= int(length):
            wire1Nowx = len(wire1Path) - 2
            wire1Nowy = len(wire1Path) - 1



            wire1Stepx = wire1Path[wire1Nowx]
            wire1Stepy = wire1Path[wire1Nowy] + 1

            wire1Path.append(wire1Stepx)
            wire1Path.append(wire1Stepy)
            wire1PathFinal.append(str(wire1Stepx) + "," + str(wire1Stepy))

            step += 1
    else:
        # down
        step = 1
        while step <= int(length):
            wire1Nowx = len(wire1Path) - 2
            wire1Nowy = len(wire1Path) - 1

            wire1Stepx = wire1Path[wire1Nowx]
            wire1Stepy = wire1Path[wire1Nowy] - 1

            wire1Path.append(wire1Stepx)
            wire1Path.append(wire1Stepy)
            wire1PathFinal.append(str(wire1Stepx) + "," + str(wire1Stepy))

            step += 1
    i += 1

print("wire1 done")
i = 0
while i < len(wire2Directions):
    direction = wire2Directions[i][0]
    length = wire2Directions[i][1:]

    if direction == "R":
        # right
        step = 1
        while step <= int(length):
            wire2Nowx = len(wire2Path) - 2
            wire2Nowy = len(wire2Path) - 1

            wire2Stepx = wire2Path[wire2Nowx] + 1
            wire2Stepy = wire2Path[wire2Nowy]

            wire2Path.append(wire2Stepx)
            wire2Path.append(wire2Stepy)
            wire2PathFinal.append(str(wire2Stepx) + "," + str(wire2Stepy))

            step += 1
    elif direction == "L":
        # left
        step = 1
        while step <= int(length):
            wire2Nowx = len(wire2Path) - 2
            wire2Nowy = len(wire2Path) - 1

            wire2Stepx = wire2Path[wire2Nowx] - 1
            wire2Stepy = wire2Path[wire2Nowy]

            wire2Path.append(wire2Stepx)
            wire2Path.append(wire2Stepy)
            wire2PathFinal.append(str(wire2Stepx) + "," + str(wire2Stepy))

            step += 1
    elif direction == "U":
        # up
        step = 1
        while step <= int(length):
            wire2Nowx = len(wire2Path) - 2
            wire2Nowy = len(wire2Path) - 1

            wire2Stepx = wire2Path[wire2Nowx]
            wire2Stepy = wire2Path[wire2Nowy] + 1

            wire2Path.append(wire2Stepx)
            wire2Path.append(wire2Stepy)
            wire2PathFinal.append(str(wire2Stepx) + "," + str(wire2Stepy))

            step += 1
    else:
        # down
        step = 1
        while step <= int(length):
            wire2Nowx = len(wire2Path) - 2
            wire2Nowy = len(wire2Path) - 1

            wire2Stepx = wire2Path[wire2Nowx]
            wire2Stepy = wire2Path[wire2Nowy] - 1

            wire2Path.append(wire2Stepx)
            wire2Path.append(wire2Stepy)
            wire2PathFinal.append(str(wire2Stepx) + "," + str(wire2Stepy))

            step += 1
    i += 1

print("wire2 done")

def manhattan_distance(x, y):
    return sum(abs(a - b) for a, b in zip(x, y))

shortest = 10000000000000.0

set1 = set(wire1PathFinal)
set2 = set(wire2PathFinal)

set3 = set1&set2

for x in set3:
    px = str.split(x, ",")[0]
    py = str.split(x, ",")[1]
    manhatton = manhattan_distance([int(px), int(py)], [0, 0])
    if manhatton < shortest:
        shortest = manhatton

print(shortest)

