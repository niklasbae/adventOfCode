import math
import csv

with open('day2/1/input.csv', 'r') as input:
    reader = csv.reader(input)
    codeList = list(reader)

x = 0
while x < len(codeList[0]):
    first = codeList[0][0 + x]
    second = codeList[0][1 + x]
    third = codeList[0][2 + x]
    fourth = codeList[0][3 + x]

    if (first == "1"):
        input1 = codeList[0][int(second)]
        input2 = codeList[0][int(third)]
        codeList[0][int(fourth)] = int(input1) + int(input2)
    elif (first == "2"):
        input1 = codeList[0][int(second)]
        input2 = codeList[0][int(third)]
        codeList[0][int(fourth)] = int(input1) * int(input2)
    else:
        break
    print(codeList)
    x += 4


print(codeList)

