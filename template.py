dayNum = ""
fullInput = False
fileName = "input"+dayNum+".txt" if fullInput else "in.txt"

# Part 1

result = 0

with open(fileName, "r") as file:
    for line in file:
        line = line.strip()

print("Part One: ", result)

# Part 2
result = 0

with open(fileName, "r") as file:
    for line in file:
        line = line.strip()

print("Part Two: ", result)