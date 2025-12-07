dayNum = "7"
fullInput = True
fileName = "input"+dayNum+".txt" if fullInput else "in.txt"

# Part 1

result = 0
beams = set()

with open(fileName, "r") as file:
    for line in file:
        line = line.strip()
        for i in range(len(line)):
            char = line[i]
            if char == "S":
                beams.add(i)
            if char == "^":
                if i in beams:
                    result += 1
                    beams.remove(i)
                beams.add(max(i-1, 0))
                beams.add(min(i+1, len(line)-1))

print("Part One: ", result)

# Part 2
result = 0
beamWeight = []

with open(fileName, "r") as file:
    for line in file:
        if len(beamWeight) == 0:
            beamWeight = [0]*len(line)
        line = line.strip()
        for i in range(len(line)):
            char = line[i] 
            if char == "S":
                beamWeight[i] = 1
            if char == "^":
                if i-1 >= 0:
                    beamWeight[i-1] += beamWeight[i]
                if i+1 < len(line):
                    beamWeight[i+1] += beamWeight[i]
                beamWeight[i] = 0

    result = sum(beamWeight)

print("Part Two: ", result)