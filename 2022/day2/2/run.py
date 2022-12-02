import math
import csv

with open('C:\\Users\\niklasp\PycharmProjects\\adventOfCode\\2022\\day2\\1\\input.csv', 'r') as input:
    reader = csv.reader(input)
    inputList = list(reader)

points = 0
loose = 'X'
draw = 'Y'
win = 'Z'
notMyRock = 'A'
notMyPaper = 'B'
notMyScissor = 'C'
rockPoints = 1
paperPoints = 2
scissorPoints = 3
winPoints = 6
drawPoints = 3

for element in inputList:
    print(element[0])
    if element[0][0] == notMyRock and element[0][2] == loose:
        points += scissorPoints
    if element[0][0] == notMyRock and element[0][2] == draw:
        points += rockPoints + drawPoints
    if element[0][0] == notMyRock and element[0][2] == win:
        points += paperPoints + winPoints
    if element[0][0] == notMyPaper and element[0][2] == loose:
        points += rockPoints
    if element[0][0] == notMyPaper and element[0][2] == draw:
        points += paperPoints + drawPoints
    if element[0][0] == notMyPaper and element[0][2] == win:
        points += scissorPoints + winPoints
    if element[0][0] == notMyScissor and element[0][2] == loose:
        points += paperPoints
    if element[0][0] == notMyScissor and element[0][2] == draw:
        points += scissorPoints + drawPoints
    if element[0][0] == notMyScissor and element[0][2] == win:
        points += rockPoints + winPoints

print(points)
