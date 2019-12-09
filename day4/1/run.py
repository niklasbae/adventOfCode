allCombinations = []
i = 402328
while i <= 864247:
    allCombinations.append(i)
    i += 1


def adjacentChecker(input):
    x = str(input)
    x1 = x[0]
    x2 = x[1]
    x3 = x[2]
    x4 = x[3]
    x5 = x[4]
    x6 = x[5]
    if(x1 == x2 or x2 == x3 or x3 == x4 or x4 == x5 or x5 == x6):
        return True

def risingChecker(input):
    x = str(input)
    x1 = x[0]
    x2 = x[1]
    x3 = x[2]
    x4 = x[3]
    x5 = x[4]
    x6 = x[5]
    if(int(x1) <= int(x2) and int(x2) <= int(x3) and int(x3) <= int(x4) and int(x4) <= int(x5) and int(x5) <= int(x6)):
        return True


comb = []

for x in allCombinations:
    if adjacentChecker(x) and risingChecker(x):
        comb.append(x)

print(len(comb))


