dayNum = ""
simpleInput = True
fileName = "input"+dayNum+".txt" if simpleInput else "in.txt"

# Part 1

result = 0

with open(fileName, "r") as file:
    for line in file:
        line = line.strip()
        print(line)

print(result)

# Part 2
result = 0

with open(fileName, "r") as file:
    for line in file:
        line = line.strip()
        print(line)

print(result)