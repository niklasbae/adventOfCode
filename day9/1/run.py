import math
import csv
import itertools


permutations = list(itertools.permutations([5, 6, 7, 8, 9]))
#permutations = [permutations[0]]
#print(permutations)

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

largest = 0
bestPermutation = permutations[0]
permutationCounter = 0
# permutation is (5, 6, 7, 8, 9)
for permutation in permutations:
    feedbackLoop = 0
    i = 1
    # i is amp number 1, 2, 3, 4, 5
    while i <= 5:
        if feedbackLoop == 0:
            with open('day9/1/input.csv', 'r') as input:
                reader = csv.reader(input)
                codeList = list(reader)
            x = 0
        else:
            if i == 1:
                x = x1
                codeList = x1codeList
                relativeBaseOffset = x1RelativeBaseOffset
            elif i == 2:
                x = x2
                codeList = x2codeList
                relativeBaseOffset = x2RelativeBaseOffset
            elif i == 3:
                x = x3
                codeList = x3codeList
                relativeBaseOffset = x3RelativeBaseOffset
            elif i == 4:
                x = x4
                codeList = x4codeList
                relativeBaseOffset = x4RelativeBaseOffset
            else:
                x = x5
                codeList = x5codeList
                relativeBaseOffset = x5RelativeBaseOffset

        inputCounter = 1
        while x < len(codeList[0]):
            firstWithParams = str(codeList[0][0 + x])
            print("firstwithparams: " + str(firstWithParams))
            print("len " + str(len(firstWithParams)))
            print("rbo " + str(relativeBaseOffset))
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
                    print(first)
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

            second = codeList[0][1 + x]
            third = codeList[0][2 + x]
            fourth = codeList[0][3 + x]
            if first == "1":
                print(codeList)
                print(second)
                if positionMode(param1):
                    input1 = codeList[0][int(second)]
                elif immidateMode(param1):
                    input1 = second
                elif relativeMode(param1):
                    rbo = int(second)+relativeBaseOffset
                    input1 = codeList[0][rbo]
                if positionMode(param2):
                    input2 = codeList[0][int(third)]
                elif immidateMode(param2):
                    input2 = third
                elif relativeMode(param2):
                    rbo = int(third)+relativeBaseOffset
                    input2 = codeList[0][rbo]
                codeList[0][int(fourth)] = int(input1) + int(input2)
                x += 4
            elif first == "2":
                if positionMode(param1):
                    input1 = codeList[0][int(second)]
                elif immidateMode(param1):
                    input1 = second
                elif relativeMode(param1):
                    rbo = int(second)+relativeBaseOffset
                    input1 = codeList[0][rbo]
                if positionMode(param2):
                    input2 = codeList[0][int(third)]
                elif immidateMode(param2):
                    input2 = third
                elif relativeMode(param2):
                    rbo = int(third)+relativeBaseOffset
                    input2 = codeList[0][rbo]
                codeList[0][int(fourth)] = int(input1) * int(input2)
                x += 4
            elif first == "3":
                if feedbackLoop == 0:
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
                else:
                    codeList[0][int(second)] = outputSignal
                print("input signal: " + str(codeList[0][int(second)]) + " on amp: " + str(i) + " on permutation: " + str(permutationCounter) + " on feedback loop: " + str(feedbackLoop))
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

                if i == 1:
                    x1 = x
                    x1codeList = codeList
                elif i == 2:
                    x2 = x
                    x2codeList = codeList
                elif i == 3:
                    x3 = x
                    x3codeList = codeList
                elif i == 4:
                    x4 = x
                    x4codeList = codeList
                else:
                    x5 = x
                    x5codeList = codeList
                break
            elif first == "5":
                if positionMode(param1):
                    if nonZero(codeList[0][int(second)]):
                        if positionMode(param2):
                            x = int(codeList[0][int(third)])
                        elif immidateMode(param2):
                            x = int(third)
                        elif relativeMode(param2):
                            rbo = int(third) + relativeBaseOffset
                            x = int(codeList[0][rbo])
                    else:
                        x += 3
                elif immidateMode(param1):
                    if nonZero(second):
                        if positionMode(param2):
                            x = int(codeList[0][int(third)])
                        elif immidateMode(param2):
                            x = int(third)
                        elif relativeMode(param2):
                            rbo = int(third) + relativeBaseOffset
                            x = int(codeList[0][rbo])
                    else:
                        x += 3
                elif relativeMode(param1):
                    rbo = int(second) + relativeBaseOffset
                    if nonZero(rbo):
                        if positionMode(param2):
                            x = int(codeList[0][int(third)])
                        elif immidateMode(param2):
                            x = int(third)
                        elif relativeMode(param2):
                            rbo = int(third) + relativeBaseOffset
                            x = int(codeList[0][rbo])
                    else:
                        x += 3
            elif first == "6":
                if positionMode(param1):
                    if not nonZero(codeList[0][int(second)]):
                        if positionMode(param2):
                            x = int(codeList[0][int(third)])
                        elif immidateMode(param2):
                            x = int(third)
                        elif relativeMode(param2):
                            rbo = int(third) + relativeBaseOffset
                            x = int(codeList[0][rbo])
                    else:
                        x += 3
                elif immidateMode(param1):
                    if not nonZero(second):
                        if positionMode(param2):
                            x = int(codeList[0][int(third)])
                        elif immidateMode(param2):
                            x = int(third)
                        elif relativeMode(param2):
                            rbo = int(third) + relativeBaseOffset
                            x = int(codeList[0][rbo])
                    else:
                        x += 3
                elif relativeMode(param1):
                    rbo = int(second) + relativeBaseOffset
                    if not nonZero(rbo):
                        if positionMode(param2):
                            x = int(codeList[0][int(third)])
                        elif immidateMode(param2):
                            x = int(third)
                        elif relativeMode(param2):
                            rbo = int(third) + relativeBaseOffset
                            x = int(codeList[0][rbo])
                    else:
                        x += 3
            elif first == "7":
                if positionMode(param1) and positionMode(param2):
                    if int(codeList[0][int(second)]) < int(codeList[0][int(third)]):
                        codeList[0][int(fourth)] = 1
                    else:
                        codeList[0][int(fourth)] = 0
                elif positionMode(param1) and immidateMode(param2):
                    if int(codeList[0][int(second)]) < int(third):
                        codeList[0][int(fourth)] = 1
                    else:
                        codeList[0][int(fourth)] = 0
                elif immidateMode(param1) and positionMode(param2):
                    if int(second) < int(codeList[0][int(third)]):
                        codeList[0][int(fourth)] = 1
                    else:
                        codeList[0][int(fourth)] = 0
                elif immidateMode(param1) and immidateMode(param2):
                    if int(second) < int(third):
                        codeList[0][int(fourth)] = 1
                    else:
                        codeList[0][int(fourth)] = 0
                elif relativeMode(param1) and relativeMode(param2):
                    rboSecond = int(second) + relativeBaseOffset
                    rboThird = int(third) + relativeBaseOffset
                    if int(codeList[0][rboSecond]) < int(codeList[0][rboThird]):
                        codeList[0][int(fourth)] = 1
                    else:
                        codeList[0][int(fourth)] = 0
                elif relativeMode(param1) and positionMode(param2):
                    rboSecond = int(second) + relativeBaseOffset
                    if int(codeList[0][rboSecond]) < int(codeList[0][third]):
                        codeList[0][int(fourth)] = 1
                    else:
                        codeList[0][int(fourth)] = 0
                elif positionMode(param1) and relativeMode(param2):
                    rboThird = int(third) + relativeBaseOffset
                    if int(codeList[0][second]) < int(codeList[0][rboThird]):
                        codeList[0][int(fourth)] = 1
                    else:
                        codeList[0][int(fourth)] = 0
                elif relativeMode(param1) and immidateMode(param2):
                    rboSecond = int(second) + relativeBaseOffset
                    if int(codeList[0][rboSecond]) < int(third):
                        codeList[0][int(fourth)] = 1
                    else:
                        codeList[0][int(fourth)] = 0
                elif immidateMode(param1) and relativeMode(param2):
                    rboThird = int(third) + relativeBaseOffset
                    if int(second) < int(codeList[0][rboThird]):
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
                elif positionMode(param1) and immidateMode(param2):
                    if int(codeList[0][int(second)]) == int(third):
                        codeList[0][int(fourth)] = 1
                    else:
                        codeList[0][int(fourth)] = 0
                elif immidateMode(param1) and positionMode(param2):
                    if int(second) == int(codeList[0][int(third)]):
                        codeList[0][int(fourth)] = 1
                    else:
                        codeList[0][int(fourth)] = 0
                elif immidateMode(param1) and immidateMode(param2):
                    if int(second) == int(third):
                        codeList[0][int(fourth)] = 1
                    else:
                        codeList[0][int(fourth)] = 0
                elif relativeMode(param1) and relativeMode(param2):
                    rboSecond = int(second) + relativeBaseOffset
                    rboThird = int(third) + relativeBaseOffset
                    if int(codeList[0][rboSecond]) == int(codeList[0][rboThird]):
                        codeList[0][int(fourth)] = 1
                    else:
                        codeList[0][int(fourth)] = 0
                elif relativeMode(param1) and positionMode(param2):
                    rboSecond = int(second) + relativeBaseOffset
                    if int(codeList[0][rboSecond]) == int(codeList[0][third]):
                        codeList[0][int(fourth)] = 1
                    else:
                        codeList[0][int(fourth)] = 0
                elif positionMode(param1) and relativeMode(param2):
                    rboThird = int(third) + relativeBaseOffset
                    if int(codeList[0][second]) == int(codeList[0][rboThird]):
                        codeList[0][int(fourth)] = 1
                    else:
                        codeList[0][int(fourth)] = 0
                elif relativeMode(param1) and immidateMode(param2):
                    rboSecond = int(second) + relativeBaseOffset
                    if int(codeList[0][rboSecond]) == int(third):
                        codeList[0][int(fourth)] = 1
                    else:
                        codeList[0][int(fourth)] = 0
                elif immidateMode(param1) and relativeMode(param2):
                    rboThird = int(third) + relativeBaseOffset
                    if int(second) == int(codeList[0][rboThird]):
                        codeList[0][int(fourth)] = 1
                    else:
                        codeList[0][int(fourth)] = 0
                x += 4
            elif first == "9":
                relativeBaseOffset = int(codeList[0][int(second)])
                print("rbooo " + str(relativeBaseOffset))
                if i == 1:
                    x1RelativeBaseOffset = relativeBaseOffset
                elif i == 2:
                    x2RelativeBaseOffset = relativeBaseOffset
                elif i == 3:
                    x3RelativeBaseOffset = relativeBaseOffset
                elif i == 4:
                    x4RelativeBaseOffset = relativeBaseOffset
                else:
                    x5RelativeBaseOffset = relativeBaseOffset
                x += 2
            else:
                i = 6
                break


        i += 1
        if i == 6:
            i = 1
            feedbackLoop += 1
    permutationCounter += 1



print(largest)
print(bestPermutation)