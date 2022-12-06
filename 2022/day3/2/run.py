import math
import csv

with open('C:\\Users\\niklasp\PycharmProjects\\adventOfCode\\2022\\day3\\1\\input.csv', 'r') as input:
    reader = csv.reader(input)
    inputList = list(reader)

commonList = []
stringList = []
counter = 1
for element in inputList:
    stringList.append(element[0])
    if counter % 3 == 0:
        commonChars1 = ''.join(
            set(stringList[0]).intersection(stringList[1])
        )
        commonChars2 = ''.join(
            set(commonChars1).intersection(stringList[2])
        )
        commonList.append(commonChars2)
        stringList = []
    counter += 1

sumPriority = 0
for element in commonList:
    if element.islower():
        #print(element + " " + str(ord(element) - 96))
        sumPriority += ord(element) - 96
    else:
        #print(element + " " + str(ord(element) - 38))
        sumPriority += ord(element) - 38

print(sumPriority)


