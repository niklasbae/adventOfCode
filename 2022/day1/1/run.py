import math
import csv

with open('C:\\Users\\niklasp\PycharmProjects\\adventOfCode\\2022\\day1\\1\\input.csv', 'r') as input:
    reader = csv.reader(input)
    calorieList = list(reader)

maxSum = 0
tempSum = 0

for element in calorieList:
    if element:
        tempSum += int(element[0])
    else:
        if tempSum > maxSum:
            maxSum = tempSum
        tempSum = 0
print(maxSum)

