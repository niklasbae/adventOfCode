import math
import csv

with open('C:\\Users\\niklasp\PycharmProjects\\adventOfCode\\2022\\day1\\1\\input.csv', 'r') as input:
    reader = csv.reader(input)
    calorieList = list(reader)

maxSum = 0
tempSum = 0
max1 = 66616
max2 = 66306
max3 = 66250

for element in calorieList:
    if element:
        tempSum += int(element[0])
    else:
        if tempSum > maxSum and tempSum < max2:
            maxSum = tempSum
        tempSum = 0
print(maxSum)
print(max1 + max2 + max3)

