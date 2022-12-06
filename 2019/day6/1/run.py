import math
import csv
import networkx as nx
import matplotlib.pyplot as plt

with open('day6/1/input.csv', 'r') as input:
    reader = csv.reader(input)
    orbitsList = list(reader)

objectsList = []

obList = []
oobList = []


for orbit in orbitsList:
    relation = str.split(orbit[0], ")")

    object = relation[0]
    orbitingObject = relation[1]


    object1 = ord(object[0])
    object2 = ord(object[1])
    object3 = ord(object[2])
    object = str(object1) + str(object2) + str(object3)

    orbitingObject1 = ord(orbitingObject[0])
    orbitingObject2 = ord(orbitingObject[1])
    orbitingObject3 = ord(orbitingObject[2])
    orbitingObject = str(orbitingObject1) + str(orbitingObject2) + str(orbitingObject3)

    objectsList.append(tuple((int(object), int(orbitingObject))))
    obList.append(int(object))
    oobList.append(int(orbitingObject))


graph = nx.from_edgelist(objectsList)

dupesOb = set([x for x in obList if obList.count(x) > 1])
oobDists = set(oobList)
dists = set(obList)

target = dists - dupesOb - oobDists

for t in target:
    target = t


sum = 0

for relation in objectsList:
    source = relation[1]
    sum += nx.shortest_path_length(graph,source=source, target=target)
print(sum)