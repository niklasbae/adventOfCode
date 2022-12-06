import math
import csv

with open('day1/1/input.csv', 'r') as input:
    reader = csv.reader(input)
    modulesList = list(reader)

totalFuel = 0

for module in modulesList:
    mass = int(module[0])
    fuel = math.floor(mass / 3) - 2
    totalFuel += fuel

print(totalFuel)