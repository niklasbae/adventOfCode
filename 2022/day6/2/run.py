import math
import csv

with open('C:\\Users\\niklasp\PycharmProjects\\adventOfCode\\2022\\day6\\1\\input.csv', 'r') as input:
    reader = csv.reader(input)
    inputList = list(reader)

element = inputList[0]

#test = ['a', 'a', 'b', 'b']
#test2 = ['a']
#print(set(test2) <= set(test))

fourList = []
counter = 1
charCounter = 0
tempList = []
okCounter = 0
for char in element[0]:
    fourList.append(char)
    print(fourList)
    if counter >= 14:
        for listElement in fourList:
            if fourList.count(listElement) > 1:
                fourList.pop(0)
                break
            else:
                okCounter += 1
    if okCounter == 14:
        charCounter = counter
        break
    okCounter = 0
    counter += 1
print(charCounter)
