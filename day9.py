from shapely.geometry import Polygon, box
dayNum = "9"
fullInput = True
fileName = "input"+dayNum+".txt" if fullInput else "in.txt"

data = []
with open(fileName, "r") as file:
    data = [[char for char in line] for line in file.read().split("\n")]

# Part 1

def size(start, end):
    xdiff = abs(start[0]-end[0])+1
    ydiff = abs(start[1]-end[1])+1
    return xdiff*ydiff

def getLine(start, end):
    if start[0] > end[0]:
        return [(x, start[1]) for x in range(end[0]+1, start[0])]
    elif end[0] > start[0]:
        return [(x, start[1]) for x in range(start[0]+1, end[0])]
    if start[1] > end[1]:
        return [(start[0], y) for y in range(end[1]+1, start[1])]
    elif end[1] > start[1]:
        return [(start[0], y) for y in range(start[1]+1, end[1])]
    return []

result = 0

# Uncomment for column-first
# data = [list(row) for row in zip(*data)]
gridSize = (0,0) # width, height
tiles = []
with open(fileName, "r") as file:
    for line in file:
        line = line.strip()
        x,y = line.split(",")
        if int(x) > gridSize[0]:
            gridSize = (int(x), gridSize[1])
        if int(y) > gridSize[1]:
            gridSize = (gridSize[0], int(y))
            
        tiles.append((int(x), int(y)))

boxes = []
for i in range(len(tiles)):
    for j in range(i+1, len(tiles)):
        start = tiles[i]
        end = tiles[j]
        boxes.append((size(start, end), start, end))

boxes.sort(key=lambda x:x[0], reverse=True)
result = boxes[0][0]

print("Part One: ", result)

# Part 2
result = 0
poly = Polygon(tiles)

for b in boxes:
    start, end = b[1], b[2]
    minx, maxx = (start[0], end[0]) if start[0] < end[0] else (end[0], start[0])
    miny, maxy = (start[1], end[1]) if start[1] < end[1] else (end[1], start[1])
    if box(minx,miny, maxx,maxy).covered_by(poly):
        result = b[0]
        break
print("Part Two: ", result)