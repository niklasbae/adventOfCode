import math
import csv

with open('day8/1/input.csv', 'r') as input:
    reader = csv.reader(input)
    pixelsList = list(reader)

width = 25
height = 6

layers = [[[]]]


pixelNo = 0
radNo = 0
layerNo = 0
while pixelNo < len(pixelsList[0][0]):



    layers[layerNo][radNo].append(pixelsList[0][0][pixelNo])

    pixelNo += 1

    if pixelNo % width == 0 and not pixelNo == 0:
        if pixelNo % (width * height) == 0:
            layerNo += 1
            radNo = 0
            layers.append([[]])
        else:
            radNo += 1
            layers[layerNo].append([])


    #print(layers)
layers.remove([[]])




fewestZeros = layers[0]
fewestZerosNumber = 9999999999
for layer in layers:
    zeroCounter = 0
    for row in layer:
        for pixel in row:
            if int(pixel) == 0:
                zeroCounter += 1
    if zeroCounter < fewestZerosNumber:
        fewestZerosNumber = zeroCounter
        fewestZeros = layer

print(layers)
print(fewestZeros)

oneCounter = 0
secondCounter = 0
for row in fewestZeros:
    for pixel in row:
        if int(pixel) == 1:
            oneCounter += 1
        if int(pixel) == 2:
            secondCounter += 1

print(oneCounter)
print(secondCounter)
output = oneCounter * secondCounter
print(fewestZeros)
print(output)



