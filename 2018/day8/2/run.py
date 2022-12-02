import math
import csv
from PIL import Image
import numpy as np

with open('day8/2/input.csv', 'r') as input:
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

#print(layers)

image = []
firstLayer = layers[0]

for layer in firstLayer:
    for row in layer:
        for pixel in row:
            image.append(pixel)
for layer in layers:
    i = 0
    for row in layer:
        for pixel in row:

            if int(image[i]) == 2:
                image[i] = pixel

            i += 1


i = 0
for pixel in image:
    if int(pixel) == 0:
        image[i] = tuple((0, 0, 0))
    else:
        image[i] = tuple((255, 255, 255))
    i += 1
#print(image)
layers = [[[]]]



pixelNo = 0
radNo = 0
layerNo = 0
while pixelNo < len(image):
    layers[layerNo][radNo].append(image[pixelNo])

    pixelNo += 1

    if pixelNo % width == 0 and not pixelNo == 0:
        if pixelNo % (width * height) == 0:
            layerNo += 1
            radNo = 0
            layers.append([[]])
        else:
            radNo += 1
            layers[layerNo].append([])

layers.remove([[]])

print(layers)

for layer in layers:
    for row in layer:
        print(row)


pixels = [
    [(0, 0, 0), (255, 255, 255), (255, 255, 255), (0, 0, 0), (0, 0, 0), (255, 255, 255), (0, 0, 0), (0, 0, 0), (0, 0, 0), (255, 255, 255), (255, 255, 255), (0, 0, 0), (0, 0, 0), (255, 255, 255), (0, 0, 0), (0, 0, 0), (255, 255, 255), (255, 255, 255), (0, 0, 0), (0, 0, 0), (255, 255, 255), (0, 0, 0), (0, 0, 0), (255, 255, 255), (0, 0, 0)],
    [(255, 255, 255), (0, 0, 0), (0, 0, 0), (255, 255, 255), (0, 0, 0), (255, 255, 255), (0, 0, 0), (0, 0, 0), (0, 0, 0), (255, 255, 255), (255, 255, 255), (0, 0, 0), (0, 0, 0), (255, 255, 255), (0, 0, 0), (255, 255, 255), (0, 0, 0), (0, 0, 0), (255, 255, 255), (0, 0, 0), (255, 255, 255), (0, 0, 0), (0, 0, 0), (255, 255, 255), (0, 0, 0)],
    [(255, 255, 255), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (255, 255, 255), (0, 0, 0), (255, 255, 255), (0, 0, 0), (255, 255, 255), (0, 0, 0), (0, 0, 0), (255, 255, 255), (0, 0, 0), (255, 255, 255), (0, 0, 0), (0, 0, 0), (255, 255, 255), (0, 0, 0), (255, 255, 255), (255, 255, 255), (255, 255, 255), (255, 255, 255), (0, 0, 0)],
    [(255, 255, 255), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (255, 255, 255), (0, 0, 0), (0, 0, 0), (255, 255, 255), (0, 0, 0), (0, 0, 0), (255, 255, 255), (0, 0, 0), (255, 255, 255), (255, 255, 255), (255, 255, 255), (255, 255, 255), (0, 0, 0), (255, 255, 255), (0, 0, 0), (0, 0, 0), (255, 255, 255), (0, 0, 0)],
    [(255, 255, 255), (0, 0, 0), (0, 0, 0), (255, 255, 255), (0, 0, 0), (0, 0, 0), (0, 0, 0), (255, 255, 255), (0, 0, 0), (0, 0, 0), (255, 255, 255), (0, 0, 0), (0, 0, 0), (255, 255, 255), (0, 0, 0), (255, 255, 255), (0, 0, 0), (0, 0, 0), (255, 255, 255), (0, 0, 0), (255, 255, 255), (0, 0, 0), (0, 0, 0), (255, 255, 255), (0, 0, 0)],
    [(0, 0, 0), (255, 255, 255), (255, 255, 255), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (255, 255, 255), (0, 0, 0), (0, 0, 0), (0, 0, 0), (255, 255, 255), (255, 255, 255), (0, 0, 0), (0, 0, 0), (255, 255, 255), (0, 0, 0), (0, 0, 0), (255, 255, 255), (0, 0, 0), (255, 255, 255), (0, 0, 0), (0, 0, 0), (255, 255, 255), (0, 0, 0)]
]

array = np.array(pixels, dtype=np.uint8)

new_image = Image.fromarray(array)
new_image.save('new.png')