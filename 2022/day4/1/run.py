import math
import csv

with open('C:\\Users\\niklasp\PycharmProjects\\adventOfCode\\2022\\day4\\1\\input.csv', 'r') as input:
    reader = csv.reader(input)
    inputList = list(reader)

#print(inputList[0])
#print(inputList[0][0])
#print(inputList[0][1])

counter = 0

for element in inputList:
    firstPair = element[0]
    secondPair = element[1]

    firstPairFirstNumber = int(firstPair.split("-")[0])
    secondPairFirstNumber = int(secondPair.split("-")[0])
    firstPairSecondNumber = int(firstPair.split("-")[1])
    secondPairSecondNumber = int(secondPair.split("-")[1])

    if firstPairFirstNumber <= secondPairFirstNumber and firstPairSecondNumber >= secondPairSecondNumber:
        counter += 1
    elif secondPairFirstNumber <= firstPairFirstNumber and secondPairSecondNumber >= firstPairSecondNumber:
        counter += 1

print(counter)