import math
import csv

with open('C:\\Users\\niklasp\PycharmProjects\\adventOfCode\\2022\\day5\\1\\input.csv', 'r') as input:
    reader = csv.reader(input)
    inputList = list(reader)

del(inputList[0:10])

l1 = ['W', 'M', 'L', 'F']
l2 = ['B', 'Z', 'V', 'M', 'F']
l3 = ['H', 'V', 'R', 'S', 'L', 'Q']
l4 = ['F', 'S', 'V', 'Q', 'P', 'M', 'T', 'J']
l5 = ['L', 'S', 'W']
l6 = ['F', 'V', 'P', 'M', 'R', 'J', 'W']
l7 = ['J', 'Q', 'C', 'P', 'N', 'R', 'F']
l8 = ['V', 'H', 'P', 'S', 'Z', 'W', 'R', 'B']
l9 = ['B', 'M', 'J', 'C', 'G', 'H', 'Z', 'W']


inputSetup = [['W', 'M', 'L', 'F'], ['B', 'Z', 'V', 'M', 'F'], ['H', 'V', 'R', 'S', 'L', 'Q'], ['F', 'S', 'V', 'Q', 'P', 'M', 'T', 'J'], ['L', 'S', 'W'], ['F', 'V', 'P', 'M', 'R', 'J', 'W'], ['J', 'Q', 'C', 'P', 'N', 'R', 'F'], ['V', 'H', 'P', 'S', 'Z', 'W', 'R', 'B'], ['B', 'M', 'J', 'C', 'G', 'H', 'Z', 'W']]
#inputSetup = [['Z', 'N'], ['M', 'C', 'D'], ['P']]
#element = inputList[0]

counter = 0
for element in inputList:
    cratesToMove = int(element[0].split(" ")[1])
    fromList = int(element[0].split(" ")[3])
    toList = int(element[0].split(" ")[5])
    moveList = []

    listToMoveFrom = inputSetup[fromList - 1]
    listToMoveTo = inputSetup[toList - 1]
    moveList = listToMoveFrom[len(listToMoveFrom) - cratesToMove:len(listToMoveFrom)]
    for y in moveList:
        listToMoveTo.append(y)
    inputSetup[fromList - 1] = listToMoveFrom[0:len(listToMoveFrom) - cratesToMove]


onTopList = []
onTopString = ""
for element in inputSetup:
    onTopList.append(element[len(element) - 1])
    onTopString = onTopString + element[len(element) - 1]

print(onTopList)
print(onTopString)
