from polyomino.board import Rectangle
from polyomino.constant import MONOMINO
from polyomino.tileset import many

dayNum = "12"
fullInput = True
fileName = "input"+dayNum+".txt" if fullInput else "in.txt"

# Part 1

result = 0

# Uncomment for column-first
# data = [list(row) for row in zip(*data)]

shapes = {}
spaces = []
with open(fileName, "r") as file:
    shapeID = None
    nextLine = file.readline().strip()
    while not "x" in nextLine:
        if ":" in nextLine:
            shapeID = int(nextLine[:nextLine.index(":")])
            shapes[shapeID] = []
            lines = [file.readline().strip() for i in range(4)]
            for i in range(3):
                for j in range(3):
                    if lines[i][j] == "#":
                        shapes[shapeID].append((i, j))
        nextLine = file.readline().strip()
    lines = [line for line in file]
    lines.insert(0, nextLine)
    for line in lines:
        line = line.strip()
        size = (int(line[:line.index("x")]), int(line[line.index("x")+1:line.index(":")]))
        presentCounts = [int(val) for val in line[line.index(":")+2:].split(" ")]
        spaces.append((size, presentCounts))

for area in spaces:
    areaSize = area[0]
    areaArea = areaSize[0]*areaSize[1]
    presentCounts = area[1]
    
    rect = Rectangle(areaSize[0], areaSize[1])

    setBase = many(MONOMINO)

    for i in range(len(presentCounts)):
        if presentCounts[i] > 0:
            setBase = setBase.and_repeated_exactly(presentCounts[i], shapes[i])

    print("Solving ", area)
    solution = None
    
    try:
        solution = rect.tile_with_set(setBase.with_reflections()).solve()
    except:
        continue

    if not solution is None:
        result += 1
print("Part One: ", result)