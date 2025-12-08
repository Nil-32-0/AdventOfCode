import math

dayNum = "8"
fullInput = True
fileName = "input"+dayNum+".txt" if fullInput else "in.txt"

data = []
with open(fileName, "r") as file:
    data = [[char for char in line] for line in file.read().split("\n")]

# Part 1

result = 0

# Uncomment for column-first
# data = [list(row) for row in zip(*data)]

def distance(pos1, pos2):
    dist = math.sqrt((pos1[0]-pos2[0])**2 + (pos1[1]-pos2[1])**2 + (pos1[2]-pos2[2])**2)
    return dist

def linked(begin, finish):
    circuit = getCircuit(begin, set())
    return finish in circuit

def getCircuit(start, nodes = set()):
    nodes.add(start)
    for node in boxes[start]:
        if node in nodes:
            continue
        getCircuit(node, nodes)
    return nodes

boxList = []
boxes = dict()

with open(fileName, "r") as file:
    for line in file:
        line = line.strip()
        x, y, z = line.split(",")
        boxList.append((int(x), int(y), int(z)))
        boxes[(int(x), int(y), int(z))] = []

lastDist = 0
lastPos = None
x = 0
total = 0
while x < len(boxList)-1:
    dist = 9*10**100
    connection = None
    for i in range(len(boxList)):
        for j in range(i+1, len(boxList)):
            start = boxList[i]
            end = boxList[j]
            if lastDist < distance(start, end) < dist:
                connection = (start, end)
                dist = distance(start, end)
    lastDist = dist
    total += 1
    if linked(connection[0], connection[1]):
        print("Skipped!", " Total:", total)
        continue
    boxes[connection[0]].append(connection[1])
    boxes[connection[1]].append(connection[0])

    lastPos = connection

    print(x)
    x += 1
print(total)

result = connection[0][0]*connection[1][0]

print("Part Two: ", result)