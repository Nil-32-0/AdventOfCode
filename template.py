dayNum = ""
fullInput = False
fileName = "input"+dayNum+".txt" if fullInput else "in.txt"

data = []
with open(fileName, "r") as file:
    data = [[char for char in line] for line in file.read().split("\n")]

# Part 1

result = 0

# Uncomment for column-first
# data = [list(row) for row in zip(*data)]

for row in data:
    for char in row:
        continue

print("Part One: ", result)

# Part 2
result = 0

for row in data:
    for char in row:
        continue

print("Part Two: ", result)