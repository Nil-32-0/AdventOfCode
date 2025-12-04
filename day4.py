dayNum = "4"
simpleInput = True
fileName = "input"+dayNum+".txt" if simpleInput else "in.txt"

# Part 1

result = 0
lines = []
with open(fileName, "r") as file:
    for line in file:
        line = line.strip()
        lineArray = []
        for char in line:
            lineArray.append(char)
        lines.append(lineArray)

rows = len(lines)
cols = len(lines[0])

def getAdjacent(i, j):
    global cols
    global rows
    adjacent = []
    if i > 0:
        adjacent.append((i-1, j))
        if j > 0:
            adjacent.append((i-1, j-1))
        if j < cols-1:
            adjacent.append((i-1, j+1))
    if j > 0:
        adjacent.append((i, j-1))
    if i < rows-1:
        adjacent.append((i+1, j))
        if j > 0:
            adjacent.append((i+1, j-1))
        if j < cols-1:
            adjacent.append((i+1, j+1))
    if j < cols-1:
        adjacent.append((i, j+1))
    return adjacent


for i in range(rows):
    for j in range(cols):
        if (lines[i][j] != "@"):
            continue
        adjacent = getAdjacent(i, j)
        neighbors = 0
        for pos in adjacent:
            if lines[pos[0]][pos[1]] == "@":
                neighbors += 1
        if neighbors < 4:
            result += 1


print(result)

# Part 2

result = 0
reLoop = True

while reLoop:
    reLoop = False
    for i in range(rows):
        for j in range(cols):
            if (lines[i][j] != "@"):
                continue
            adjacent = getAdjacent(i, j)
            neighbors = 0
            for pos in adjacent:
                if lines[pos[0]][pos[1]] == "@":
                    neighbors += 1
            if neighbors < 4:
                lines[i][j] = "."
                result += 1
                reLoop = True
print(result)