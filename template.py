dayNum = ""
fullInput = True
fileName = "input"+dayNum+".txt" if simpleInput else "in.txt"

# Part 1

result = 0

with open(fileName, "r") as file:
    for line in file:
        line = line.strip()
        print(line)

print("Part One: ", result)

# Part 2
result = 0

with open(fileName, "r") as file:
    for line in file:
        line = line.strip()
        print(line)

print("Part Two: ", result)