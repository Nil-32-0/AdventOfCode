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

def getCircuit(start, nodes = set()):
    nodes.add(start)
    for node in circuits[start]:
        if node in nodes:
            continue
        getCircuit(node, nodes)
    return nodes

def linked(start, end, links = set()):
    links.add(start)
    for circuit in circuits[start]:
        if circuit in links:
            continue
        if linked(circuit, end):
            return True
    return False

boxList = []
circuits = dict()
foundConnections = []

with open(fileName, "r") as file:
    for line in file:
        line = line.strip()
        x, y, z = line.split(",")
        circuits[(int(x), int(y), int(z))] = []
        boxList.append((int(x), int(y), int(z)))

connections = 1000
foundConnections = []
for i in range(len(boxList)):
    for j in range(i+1, len(boxList)):
        start = boxList[i]
        end = boxList[j]
        dist = distance(start, end)
        if len(foundConnections) < connections:
            foundConnections.append((start, end, dist))
            if len(foundConnections) == connections:
                foundConnections.sort(key=lambda x: x[2])
            continue
        for x in range(len(foundConnections)):
            enDist = foundConnections[x][2]
            if dist < enDist:
                foundConnections.insert(x, (start, end, dist))
                foundConnections.pop()
                break
            
for connection in foundConnections:
    start = connection[0]
    end = connection[1]
    if not linked(start, end):
        circuits[start].append(end)
        circuits[end].append(start)
    
checkedCircuits = [None]*3
circuitLengths = [0]*3
checkCircuits = 3

for i in range(checkCircuits):
    length = 0
    circ = None
    for circuit in circuits.keys():
        totalCirc = set()
        getCircuit(circuit, totalCirc)
        if totalCirc not in checkedCircuits and len(totalCirc) > length:
            length = len(totalCirc)
            circ = totalCirc
    checkedCircuits[i] = circ
    circuitLengths[i] = length

result = 1
for length in circuitLengths:
    result *= length

print("Part One: ", result)

# Part 2
result = 0

for row in data:
    for char in row:
        continue

print("Part Two: ", result)