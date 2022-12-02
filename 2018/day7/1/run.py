import math
import csv
import itertools


permutations = list(itertools.permutations([4, 3, 2, 1, 0]))

def positionMode(parameter):
    if int(parameter) == 0:
        return True
    else:
        return False

def nonZero(parameter):
    if int(parameter) == 0:
        return False
    else:
        return True

largest = 0
bestPermutation = permutations[0]
permutationCounter = 0
for permutation in permutations:
    i = 1
    while i <= 5:
        inputCounter = 1
        with open('day7/1/input.csv', 'r') as input:
            reader = csv.reader(input)
            codeList = list(reader)
        x = 0
        while x < len(codeList[0]):
            firstWithParams = str(codeList[0][0 + x])
            if len(firstWithParams) == 1:
                first = firstWithParams
                param1 = 0
                param2 = 0
                param3 = 0
            elif len(firstWithParams) == 2:
                if firstWithParams[1] == 9:
                    first = "99"
                else:
                    first = firstWithParams[1]
                    param1 = 0
                    param2 = 0
                    param3 = 0
            elif len(firstWithParams) == 3:
                if firstWithParams[1] == 9:
                    first = "99"
                else:
                    first = firstWithParams[2]
                    param1 = firstWithParams[0]
                    param2 = 0
                    param3 = 0
            elif len(firstWithParams) == 4:
                if firstWithParams[2] == 9:
                    first = "99"
                else:
                    first = firstWithParams[3]
                    param1 = firstWithParams[1]
                    param2 = firstWithParams[0]
                    param3 = 0
            else:
                if firstWithParams[3] == 9:
                    first = "99"
                else:
                    first = firstWithParams[4]
                    param1 = firstWithParams[2]
                    param2 = firstWithParams[1]
                    param3 = firstWithParams[0]

            second = codeList[0][1 + x]
            third = codeList[0][2 + x]
            fourth = codeList[0][3 + x]
            if first == "1":
                if positionMode(param1):
                    input1 = codeList[0][int(second)]
                else:
                    input1 = second
                if positionMode(param2):
                    input2 = codeList[0][int(third)]
                else:
                    input2 = third
                codeList[0][int(fourth)] = int(input1) + int(input2)
                x += 4
            elif first == "2":
                if positionMode(param1):
                    input1 = codeList[0][int(second)]
                else:
                    input1 = second
                if positionMode(param2):
                    input2 = codeList[0][int(third)]
                else:
                    input2 = third
                codeList[0][int(fourth)] = int(input1) * int(input2)
                x += 4
            elif first == "3":
                if i == 1:
                    if inputCounter == 1:
                        codeList[0][int(second)] = permutation[i-1]
                    else:
                        codeList[0][int(second)] = 0
                else:
                    if inputCounter == 1:
                        codeList[0][int(second)] = permutation[i-1]
                    else:
                        codeList[0][int(second)] = outputSignal
                print("input signal: " + str(codeList[0][int(second)]) + " on amp: " + str(i) + " on permutation: " + str(permutationCounter))

                inputCounter += 1
                x += 2
            elif first == "4":
                print("output signal: " + str(codeList[0][int(second)]))
                outputSignal = int(codeList[0][int(second)])
                if i == 5:
                    if outputSignal > largest:
                        largest = outputSignal
                        bestPermutation = permutation
                x += 2
            elif first == "5":
                if positionMode(param1):
                    if nonZero(codeList[0][int(second)]):
                        if positionMode(param2):
                            x = int(codeList[0][int(third)])
                        else:
                            x = int(third)
                    else:
                        x += 3
                else:
                    if nonZero(second):
                        if positionMode(param2):
                            x = int(codeList[0][int(third)])
                        else:
                            x = int(third)
                    else:
                        x += 3
            elif first == "6":
                if positionMode(param1):
                    if not nonZero(codeList[0][int(second)]):
                        if positionMode(param2):
                            x = int(codeList[0][int(third)])
                        else:
                            x = int(third)
                    else:
                        x += 3
                else:
                    if not nonZero(second):
                        if positionMode(param2):
                            x = int(codeList[0][int(third)])
                        else:
                            x = int(third)
                    else:
                        x += 3
            elif first == "7":
                if positionMode(param1) and positionMode(param2):
                    if int(codeList[0][int(second)]) < int(codeList[0][int(third)]):
                        codeList[0][int(fourth)] = 1
                    else:
                        codeList[0][int(fourth)] = 0
                elif positionMode(param1) and not positionMode(param2):
                    if int(codeList[0][int(second)]) < int(third):
                        codeList[0][int(fourth)] = 1
                    else:
                        codeList[0][int(fourth)] = 0
                elif not positionMode(param1) and positionMode(param2):
                    if int(second) < int(codeList[0][int(third)]):
                        codeList[0][int(fourth)] = 1
                    else:
                        codeList[0][int(fourth)] = 0
                else:
                    if int(second) < int(third):
                        codeList[0][int(fourth)] = 1
                    else:
                        codeList[0][int(fourth)] = 0
                x += 4
            elif first == "8":
                if positionMode(param1) and positionMode(param2):
                    if int(codeList[0][int(second)]) == int(codeList[0][int(third)]):
                        codeList[0][int(fourth)] = 1
                    else:
                        codeList[0][int(fourth)] = 0
                elif positionMode(param1) and not positionMode(param2):
                    if int(codeList[0][int(second)]) == int(third):
                        codeList[0][int(fourth)] = 1
                    else:
                        codeList[0][int(fourth)] = 0
                elif not positionMode(param1) and positionMode(param2):
                    if int(second) == int(codeList[0][int(third)]):
                        codeList[0][int(fourth)] = 1
                    else:
                        codeList[0][int(fourth)] = 0
                else:
                    if int(second) == int(third):
                        codeList[0][int(fourth)] = 1
                    else:
                        codeList[0][int(fourth)] = 0
                x += 4
            else:
                break
        i += 1
    permutationCounter += 1



print(largest)
print(permutation)