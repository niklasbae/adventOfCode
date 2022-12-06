import math
import csv

with open('C:\\Users\\niklasp\PycharmProjects\\adventOfCode\\2022\\day6\\1\\input.csv', 'r') as input:
    reader = csv.reader(input)
    inputList = list(reader)

element = inputList[0]

test = ['a', 'a', 'b', 'b']
#print(test)
test.pop(0)
#print(test)
#print(test[1] == test[2])

fourList = []
counter = 1
charCounter = 0
for char in element[0]:
    fourList.append(char)
    #print(fourList)
    if counter >= 4:
        first = fourList[0]
        second = fourList[1]
        third = fourList[2]
        fourth = fourList[3]
        if first == second or first == third or first == fourth or second == third or second == fourth or third == fourth:
            fourList.pop(0)
        else:
            charCounter = counter
            break
    counter += 1
print(charCounter)
