import math
import csv

with open('C:\\Users\\niklasp\PycharmProjects\\adventOfCode\\2022\\day3\\1\\input.csv', 'r') as input:
    reader = csv.reader(input)
    inputList = list(reader)

commonList = []
for element in inputList:
    # substring from index 0 to length of string / 2
    string1 = element[0][0:(int(len(element[0]) / 2))]
    # substring from index length of string / 2 to length of string
    string2 = element[0][(int(len(element[0]) / 2)):len(element[0])]
    commonChars = ''.join(
        set(string1).intersection(string2)
    )
    commonList.append(commonChars)

sumPriority = 0
for element in commonList:
    if element.islower():
        #print(element + " " + str(ord(element) - 96))
        sumPriority += ord(element) - 96
    else:
        #print(element + " " + str(ord(element) - 38))
        sumPriority += ord(element) - 38

print(sumPriority)
