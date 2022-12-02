import math
import csv

with open('C:\\Users\\niklasp\PycharmProjects\\adventOfCode\\2022\\day2\\1\\input.csv', 'r') as input:
    reader = csv.reader(input)
    inputList = list(reader)

points = 0
myRock = 'X'
myPaper = 'Y'
myScissor = 'Z'
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
    if element[0][0] == notMyRock and element[0][2] == myRock:
        points += rockPoints + drawPoints
    if element[0][0] == notMyRock and element[0][2] == myPaper:
        points += paperPoints + winPoints
    if element[0][0] == notMyRock and element[0][2] == myScissor:
        points += scissorPoints
    if element[0][0] == notMyPaper and element[0][2] == myRock:
        points += rockPoints
    if element[0][0] == notMyPaper and element[0][2] == myPaper:
        points += paperPoints + drawPoints
    if element[0][0] == notMyPaper and element[0][2] == myScissor:
        points += scissorPoints + winPoints
    if element[0][0] == notMyScissor and element[0][2] == myRock:
        points += rockPoints + winPoints
    if element[0][0] == notMyScissor and element[0][2] == myPaper:
        points += paperPoints
    if element[0][0] == notMyScissor and element[0][2] == myScissor:
        points += scissorPoints + drawPoints

print(points)
