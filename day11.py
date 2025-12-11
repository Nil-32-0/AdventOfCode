dayNum = "11"
fullInput = True
fileName = "input"+dayNum+".txt" if fullInput else "in.txt"

data = []
with open(fileName, "r") as file:
    data = [[char for char in line] for line in file.read().split("\n")]

# Part 1

result = 0

# Uncomment for column-first
# data = [list(row) for row in zip(*data)]

nodes = {}
reverseNodes = {}
with open(fileName, "r") as file:
    for line in file:
        line = line.strip()
        name = line[:line.index(":")]
        outputs = line[line.index(":")+2:].split(" ")
        nodes[name] = outputs
        for output in outputs:
            if output not in reverseNodes.keys():
                reverseNodes[output] = []
            reverseNodes[output].append(name)

trueDead = set()
nodesToScan = set()
nodesToScan.update(reverseNodes["out"])

while len(nodesToScan) > 0:
    node = nodesToScan.pop()
    dead = True
    for n in nodes[node]:
        if n != "out" and not n in trueDead:
            dead = False
        if n == "dac" or n == "fft":
            dead = False
    if dead:
        trueDead.add(node)
        if node in reverseNodes.keys():
            nodesToScan.update(reverseNodes[node])

tempDead = set()
nodesToScan = set()
nodesToScan.update(reverseNodes["out"])
nodesToScan.update(reverseNodes["dac"])

while len(nodesToScan) > 0:
    node = nodesToScan.pop()
    dead = True
    for n in nodes[node]:
        if n != "out" and n != "dac" and not n in trueDead and not n in tempDead:
            dead = False
        if n == "fft":
            dead = False
    if dead:
        tempDead.add(node)
        if node in reverseNodes.keys():
            nodesToScan.update(reverseNodes[node])

nodesToVisit = []
nodesToVisit.extend(nodes["you"])

bigtotal=0

while len(nodesToVisit) > 0:
    nextNode = nodesToVisit.pop(0)
    futureNodes = nodes[nextNode]
    for node in futureNodes:
        if node == "out":
            result += 1
        else:
            nodesToVisit.append(node)

print("Part One: ", result)
result = 0

nodesToVisit = []
nodesToVisit.extend(nodes['svr'])

while len(nodesToVisit) > 0:
    nextNode = nodesToVisit.pop()
    futureNodes = nodes[nextNode]
    for node in futureNodes:
        if node == "fft":
            result += 1
        elif node in tempDead or node in trueDead:
            continue
        else:
            nodesToVisit.append(node)

bigtotal += result
print("Segment One:", bigtotal)
result = 0

nodesToVisit = []
nodesToVisit.extend(nodes['fft'])

while len(nodesToVisit) > 0:
    nextNode = nodesToVisit.pop()
    futureNodes = nodes[nextNode]
    for node in futureNodes:
        if node == "dac":
            result += 1
        elif node in trueDead:
            continue
        else:
            nodesToVisit.append(node)

bigtotal *= result
print("Segment Two:", result)
result = 0

nodesToVisit = []
nodesToVisit.extend(nodes['dac'])

while len(nodesToVisit) > 0:
    nextNode = nodesToVisit.pop()
    futureNodes = nodes[nextNode]
    for node in futureNodes:
        if node == "out":
            result += 1
        else:
            nodesToVisit.append(node)

bigtotal *= result
print("Segment Three:", result)

print("Part Two: ", bigtotal)

# Part 2
result = 0
# FFT occurs first

