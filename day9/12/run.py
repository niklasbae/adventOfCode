import math
import csv
from collections import defaultdict
import time

with open('day9/12/input.csv', 'r') as input:
    reader = csv.reader(input)
    codeList = list(reader)

test = defaultdict(int)

i = 0
for code in codeList[0]:
    test[i] = int(code)
    i += 1

def positionMode(parameter):
    if int(parameter) == 0:
        return True
    else:
        return False

def immidateMode(parameter):
    if int(parameter) == 1:
        return True
    else:
        return False

def relativeMode(parameter):
    if int(parameter) == 2:
        return True
    else:
        return False

def nonZero(parameter):
    if int(parameter) == 0:
        return False
    else:
        return True



x = 0
y = 0
relativeBaseOffset = 0
while x < len(test)*1000:
    firstWithParams = str(test[0 + x])
    if len(firstWithParams) == 1:
        first = firstWithParams
        param1 = 0
        param2 = 0
        param3 = 0
    elif len(firstWithParams) == 2:
        if firstWithParams[1] == "9":
            first = "99"
        else:
            first = firstWithParams[1]
            param1 = 0
            param2 = 0
            param3 = 0
    elif len(firstWithParams) == 3:
        if firstWithParams[1] == "9":
            first = "99"
        else:
            first = firstWithParams[2]
            param1 = firstWithParams[0]
            param2 = 0
            param3 = 0
    elif len(firstWithParams) == 4:
        if firstWithParams[2] == "9":
            first = "99"
        else:
            first = firstWithParams[3]
            param1 = firstWithParams[1]
            param2 = firstWithParams[0]
            param3 = 0
    else:
        if firstWithParams[3] == "9":
            first = "99"
        else:
            first = firstWithParams[4]
            param1 = firstWithParams[2]
            param2 = firstWithParams[1]
            param3 = firstWithParams[0]

    second = test[1 + x]
    third = test[2 + x]
    fourth = test[3 + x]
    if first == "1":
        if positionMode(param3):
            if positionMode(param1):
                input1 = test[int(second)]
            elif immidateMode(param1):
                input1 = second
            elif relativeMode(param1):
                rbo = int(second) + relativeBaseOffset
                input1 = test[rbo]
            if positionMode(param2):
                input2 = test[int(third)]
            elif immidateMode(param2):
                input2 = third
            elif relativeMode(param2):
                rbo = int(third) + relativeBaseOffset
                input2 = test[rbo]
            test[int(fourth)] = int(input1) + int(input2)
        elif relativeMode(param3):
            if positionMode(param1):
                input1 = test[int(second)]
            elif immidateMode(param1):
                input1 = second
            elif relativeMode(param1):
                rbo = int(second) + relativeBaseOffset
                input1 = test[rbo]
            if positionMode(param2):
                input2 = test[int(third)]
            elif immidateMode(param2):
                input2 = third
            elif relativeMode(param2):
                rbo = int(third) + relativeBaseOffset
                input2 = test[rbo]
            rbo = int(fourth) + relativeBaseOffset
            test[rbo] = int(input1) + int(input2)
        x += 4
    elif first == "2":
        #print(param3)
        if positionMode(param3):
            if positionMode(param1):
                input1 = test[int(second)]
            elif immidateMode(param1):
                input1 = second
            elif relativeMode(param1):
                rbo = int(second) + relativeBaseOffset
                input1 = test[rbo]
            if positionMode(param2):
                input2 = test[int(third)]
            elif immidateMode(param2):
                input2 = third
            elif relativeMode(param2):
                rbo = int(third) + relativeBaseOffset
                input2 = test[rbo]
            test[int(fourth)] = int(input1) * int(input2)
        elif relativeMode(param3):
            if positionMode(param1):
                input1 = test[int(second)]
            elif immidateMode(param1):
                input1 = second
            elif relativeMode(param1):
                rbo = int(second) + relativeBaseOffset
                input1 = test[rbo]
            if positionMode(param2):
                input2 = test[int(third)]
            elif immidateMode(param2):
                input2 = third
            elif relativeMode(param2):
                rbo = int(third) + relativeBaseOffset
                input2 = test[rbo]
            rbo = int(fourth) + relativeBaseOffset
            test[rbo] = int(input1) * int(input2)
        x += 4
    elif first == "3":
        if positionMode(param1):
            test[int(second)] = 2
        elif relativeMode(param1):
            rbo = int(second) + relativeBaseOffset
            test[rbo] = 2
        x += 2
    elif first == "4":
        if positionMode(param1):
            print(test[int(second)])
        elif immidateMode((param1)):
            print(second)
        elif relativeMode(param1):
            rbo = int(second) + relativeBaseOffset
            print(test[rbo])
        x += 2
    elif first == "5":
        if positionMode(param1):
            if nonZero(test[int(second)]):
                if positionMode(param2):
                    x = int(test[int(third)])
                elif immidateMode(param2):
                    x = int(third)
                elif relativeMode(param2):
                    rbo = int(third) + relativeBaseOffset
                    x = int(test[rbo])
            else:
                x += 3
        elif immidateMode(param1):
            if nonZero(second):
                if positionMode(param2):
                    x = int(test[int(third)])
                elif immidateMode(param2):
                    x = int(third)
                elif relativeMode(param2):
                    rbo = int(third) + relativeBaseOffset
                    x = int(test[rbo])
            else:
                x += 3
        elif relativeMode(param1):
            rbo = int(second) + relativeBaseOffset
            if nonZero(test[rbo]):
                if positionMode(param2):
                    x = int(test[int(third)])
                elif immidateMode(param2):
                    x = int(third)
                elif relativeMode(param2):
                    rbo = int(third) + relativeBaseOffset
                    x = int(test[rbo])
            else:
                x += 3
    elif first == "6":
        if positionMode(param1):
            if not nonZero(test[int(second)]):
                if positionMode(param2):
                    x = int(test[int(third)])
                elif immidateMode(param2):
                    x = int(third)
                elif relativeMode(param2):
                    rbo = int(third) + relativeBaseOffset
                    x = int(test[rbo])
            else:
                x += 3
        elif immidateMode(param1):
            if not nonZero(second):
                if positionMode(param2):
                    x = int(test[int(third)])
                elif immidateMode(param2):
                    x = int(third)
                elif relativeMode(param2):
                    rbo = int(third) + relativeBaseOffset
                    x = int(test[rbo])
            else:
                x += 3
        elif relativeMode(param1):
            rbo = int(second) + relativeBaseOffset
            if not nonZero(test[rbo]):
                if positionMode(param2):
                    x = int(test[int(third)])
                elif immidateMode(param2):
                    x = int(third)
                elif relativeMode(param2):
                    rbo = int(third) + relativeBaseOffset
                    x = int(test[rbo])
            else:
                x += 3
    elif first == "7":
        if positionMode(param3):
            if positionMode(param1) and positionMode(param2):
                if int(test[int(second)]) < int(test[int(third)]):
                    test[int(fourth)] = 1
                else:
                    test[int(fourth)] = 0
            elif positionMode(param1) and immidateMode(param2):
                if int(test[int(second)]) < int(third):
                    test[int(fourth)] = 1
                else:
                    test[int(fourth)] = 0
            elif immidateMode(param1) and positionMode(param2):
                if int(second) < int(test[int(third)]):
                    test[int(fourth)] = 1
                else:
                    test[int(fourth)] = 0
            elif immidateMode(param1) and immidateMode(param2):
                if int(second) < int(third):
                    test[int(fourth)] = 1
                else:
                    test[int(fourth)] = 0
            elif relativeMode(param1) and relativeMode(param2):
                rboSecond = int(second) + relativeBaseOffset
                rboThird = int(third) + relativeBaseOffset
                if int(test[rboSecond]) < int(test[rboThird]):
                    test[int(fourth)] = 1
                else:
                    test[int(fourth)] = 0
            elif relativeMode(param1) and positionMode(param2):
                rboSecond = int(second) + relativeBaseOffset
                if int(test[rboSecond]) < int(test[third]):
                    test[int(fourth)] = 1
                else:
                    test[int(fourth)] = 0
            elif positionMode(param1) and relativeMode(param2):
                rboThird = int(third) + relativeBaseOffset
                if int(test[second]) < int(test[rboThird]):
                    test[int(fourth)] = 1
                else:
                    test[int(fourth)] = 0
            elif relativeMode(param1) and immidateMode(param2):
                rboSecond = int(second) + relativeBaseOffset
                if int(test[rboSecond]) < int(third):
                    test[int(fourth)] = 1
                else:
                    test[int(fourth)] = 0
            elif immidateMode(param1) and relativeMode(param2):
                rboThird = int(third) + relativeBaseOffset
                if int(second) < int(test[rboThird]):
                    test[int(fourth)] = 1
                else:
                    test[int(fourth)] = 0
        elif relativeMode(param3):
            rbo = int(fourth) + relativeBaseOffset
            if positionMode(param1) and positionMode(param2):
                if int(test[int(second)]) < int(test[int(third)]):
                    test[int(rbo)] = 1
                else:
                    test[int(rbo)] = 0
            elif positionMode(param1) and immidateMode(param2):
                if int(test[int(second)]) < int(third):
                    test[int(rbo)] = 1
                else:
                    test[int(rbo)] = 0
            elif immidateMode(param1) and positionMode(param2):
                if int(second) < int(test[int(third)]):
                    test[int(rbo)] = 1
                else:
                    test[int(rbo)] = 0
            elif immidateMode(param1) and immidateMode(param2):
                if int(second) < int(third):
                    test[int(rbo)] = 1
                else:
                    test[int(rbo)] = 0
            elif relativeMode(param1) and relativeMode(param2):
                rboSecond = int(second) + relativeBaseOffset
                rboThird = int(third) + relativeBaseOffset
                if int(test[rboSecond]) < int(test[rboThird]):
                    test[int(rbo)] = 1
                else:
                    test[int(rbo)] = 0
            elif relativeMode(param1) and positionMode(param2):
                rboSecond = int(second) + relativeBaseOffset
                if int(test[rboSecond]) < int(test[int(third)]):
                    test[int(rbo)] = 1
                else:
                    test[int(rbo)] = 0
            elif positionMode(param1) and relativeMode(param2):
                rboThird = int(third) + relativeBaseOffset
                if int(test[int(second)]) < int(test[rboThird]):
                    test[int(rbo)] = 1
                else:
                    test[int(rbo)] = 0
            elif relativeMode(param1) and immidateMode(param2):
                rboSecond = int(second) + relativeBaseOffset
                if int(test[rboSecond]) < int(third):
                    test[int(rbo)] = 1
                else:
                    test[int(rbo)] = 0
            elif immidateMode(param1) and relativeMode(param2):
                rboThird = int(third) + relativeBaseOffset
                if int(second) < int(test[rboThird]):
                    test[int(rbo)] = 1
                else:
                    test[int(rbo)] = 0
        x += 4
    elif first == "8":
        if positionMode(param3):
            if positionMode(param1) and positionMode(param2):
                if int(test[int(second)]) == int(test[int(third)]):
                    test[int(fourth)] = 1
                else:
                    test[int(fourth)] = 0
            elif positionMode(param1) and immidateMode(param2):
                if int(test[int(second)]) == int(third):
                    test[int(fourth)] = 1
                else:
                    test[int(fourth)] = 0
            elif immidateMode(param1) and positionMode(param2):
                if int(second) == int(test[int(third)]):
                    test[int(fourth)] = 1
                else:
                    test[int(fourth)] = 0
            elif immidateMode(param1) and immidateMode(param2):
                if int(second) == int(third):
                    test[int(fourth)] = 1
                else:
                    test[int(fourth)] = 0
            elif relativeMode(param1) and relativeMode(param2):
                rboSecond = int(second) + relativeBaseOffset
                rboThird = int(third) + relativeBaseOffset
                if int(test[rboSecond]) == int(test[rboThird]):
                    test[int(fourth)] = 1
                else:
                    test[int(fourth)] = 0
            elif relativeMode(param1) and positionMode(param2):
                rboSecond = int(second) + relativeBaseOffset
                if int(test[rboSecond]) == int(test[int(third)]):
                    test[int(fourth)] = 1
                else:
                    test[int(fourth)] = 0
            elif positionMode(param1) and relativeMode(param2):
                rboThird = int(third) + relativeBaseOffset
                if int(test[int(second)]) == int(test[rboThird]):
                    test[int(fourth)] = 1
                else:
                    test[int(fourth)] = 0
            elif relativeMode(param1) and immidateMode(param2):
                rboSecond = int(second) + relativeBaseOffset
                if int(test[rboSecond]) == int(third):
                    test[int(fourth)] = 1
                else:
                    test[int(fourth)] = 0
            elif immidateMode(param1) and relativeMode(param2):
                rboThird = int(third) + relativeBaseOffset
                if int(second) == int(test[rboThird]):
                    test[int(fourth)] = 1
                else:
                    test[int(fourth)] = 0
        elif relativeMode(param3):
            rbo = int(fourth) + relativeBaseOffset
            if positionMode(param1) and positionMode(param2):
                if int(test[int(second)]) == int(test[int(third)]):
                    test[int(rbo)] = 1
                else:
                    test[int(rbo)] = 0
            elif positionMode(param1) and immidateMode(param2):
                if int(test[int(second)]) == int(third):
                    test[int(rbo)] = 1
                else:
                    test[int(rbo)] = 0
            elif immidateMode(param1) and positionMode(param2):
                if int(second) == int(test[int(third)]):
                    test[int(rbo)] = 1
                else:
                    test[int(rbo)] = 0
            elif immidateMode(param1) and immidateMode(param2):
                if int(second) == int(third):
                    test[int(rbo)] = 1
                else:
                    test[int(rbo)] = 0
            elif relativeMode(param1) and relativeMode(param2):
                rboSecond = int(second) + relativeBaseOffset
                rboThird = int(third) + relativeBaseOffset
                if int(test[rboSecond]) == int(test[rboThird]):
                    test[int(rbo)] = 1
                else:
                    test[int(rbo)] = 0
            elif relativeMode(param1) and positionMode(param2):
                rboSecond = int(second) + relativeBaseOffset
                if int(test[rboSecond]) == int(test[int(third)]):
                    test[int(rbo)] = 1
                else:
                    test[int(rbo)] = 0
            elif positionMode(param1) and relativeMode(param2):
                rboThird = int(third) + relativeBaseOffset
                if int(test[int(second)]) == int(test[rboThird]):
                    test[int(rbo)] = 1
                else:
                    test[int(rbo)] = 0
            elif relativeMode(param1) and immidateMode(param2):
                rboSecond = int(second) + relativeBaseOffset
                if int(test[rboSecond]) == int(third):
                    test[int(rbo)] = 1
                else:
                    test[int(rbo)] = 0
            elif immidateMode(param1) and relativeMode(param2):
                rboThird = int(third) + relativeBaseOffset
                if int(second) == int(test[rboThird]):
                    test[int(rbo)] = 1
                else:
                    test[int(rbo)] = 0
        x += 4
    elif first == "9":
        if positionMode(param1):
            relativeBaseOffset += int(test[int(second)])
        elif immidateMode((param1)):
            relativeBaseOffset += int(second)
        elif relativeMode(param1):
            rbo = int(second) + relativeBaseOffset
            relativeBaseOffset += int(test[int(rbo)])
        x += 2
    elif first == "99":
        break
    y += 1
# print(test)



