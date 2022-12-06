j = 2
k = 2
while k < len(wire1Path):
    j = 2
    while j < len(wire2Path):
        p1x = wire1Path[k]
        p1y = wire1Path[k+1]
        p2x = wire2Path[j]
        p2y = wire2Path[j+1]
        if p1x == p2x and p1y == p2y:
            manhatton = manhattan_distance([p1x, p1y], [0,0])
            print("yey")
            if manhatton < shortest:
                shortest = manhatton
                px = p1x
                py = p1y
        j += 2
    k += 2
    print(k)