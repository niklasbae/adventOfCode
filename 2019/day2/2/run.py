import math
import csv

with open('day2/2/input.csv', 'r') as input:
    reader = csv.reader(input)
    codeList = list(reader)

y = 0
while y < 100:
    z = 0
    while z < 100:
        x = 0
        with open('day2/2/input.csv', 'r') as input:
            reader = csv.reader(input)
            codeList = list(reader)
        codeList[0][1] = str(z)
        codeList[0][2] = str(y)
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
                if(codeList[0][0] == 19690720):
                    noun = codeList[0][1]
                    verb = codeList[0][2]
                    y = 101
                    z = 101
                break
            x += 4
        z += 1
    y += 1


print(100 * int(noun) + int(verb))

