from pulp import *

dayNum = "10"
fullInput = True
fileName = "input"+dayNum+".txt" if fullInput else "in.txt"

# data = []
# with open(fileName, "r") as file:
#     data = [[char for char in line] for line in file.read().split("\n")]

# Part 1

result = 0

# Uncomment for column-first
# data = [list(row) for row in zip(*data)]

machines = []
with open(fileName, "r") as file:
    for line in file:
        line = line.strip()
        endDisplayIndex = line.index("]")
        display = [char for char in line[1:endDisplayIndex]]
        startJoltIndex = line.index("{")
        joltage = line[startJoltIndex+1:-1].split(",")
        rawWirings = line[endDisplayIndex+2:startJoltIndex].split(" ")
        wirings = []
        for wire in rawWirings:
            if wire != "":
                wirings.append([int(char) for char in wire[1:-1].split(",")])
        machines.append([display, wirings, joltage])
maxes = []
for machine in machines:
    wiring = machine[1]
    buttonPressConfigs = []
    for i in range(2**len(machine[1])):
        l = str(len(machine[1]))
        base = "{0:0"+l+"b}"
        val = base.format(i)
        buttonPressConfigs.append([char for char in val])
    buttonPressConfigs.sort(key=lambda x: sum([int(y) for y in x]))
    for config in buttonPressConfigs:
        display = ["."]*len(machine[0])
        for i in range(len(config)):
            changes = wiring[i]
            for change in changes:
                if config[i] == "1":
                    display[change] = "#" if display[change] == "." else "."
        if display == machine[0]:
            result += sum([int(y) for y in config])
            break

print("Part One: ", result)

# Part 2
result = 0

solutions = []
solutionNums = []

for machine in machines:
    prob = LpProblem("Prob", LpMinimize)

    variables = []
    for i in range(len(machine[1])):
        var = LpVariable("Button_"+str(i), lowBound=0, cat='Integer')
        variables.append(var)
    prob += sum(variables)
    for i in range(len(machine[2])):
        target = int(machine[2][i]) # Target joltage
        coefficients = LpVariable.dict("Coefficients", [])
        for j in range(len(variables)):
            coefficients[j] = 1 if i in machine[1][j] else 0
        
        equation = [variables[i] * coefficients[i] for i in range(len(variables))]
        
        constraint = LpConstraint(lpSum(equation), LpConstraintEQ, "Ticker "+str(i)+" Switches", target) 
        
        prob += constraint
    
    prob.solve()

    solutions.append("\n".join([v.name+"="+str(v.varValue) for v in prob.variables()]))
    solutionNums.append([v.varValue for v in prob.variables()])

print("\n\n".join(solutions))
print(solutionNums)
print(sum([sum(x) for x in solutionNums]))

print("Part Two: ", result)