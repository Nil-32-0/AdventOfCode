dayNum = "6"
fullInput = True
fileName = "input"+dayNum+".txt" if fullInput else "in.txt"

# Part 1

result = 0
columns = []
operators = []

with open(fileName, "r") as file:
    nums = True
    for line in file:
        line = line.strip()
        line = line.split(" ")
        trueLine = []
        for entry in line:
            if entry != "":
                trueLine.append(entry)
        line = trueLine
        if (len(columns) == 0):
            for entry in line:
                columns.append([])
        if (line[0] == "+" or line[0] == "*"):
            nums = False
        if nums:
            for i in range(len(line)):
                columns[i].append(int(line[i]))
        else:
            for op in line:
                operators.append(op)

    for i in range(len(columns)):
        nums = columns[i]
        operator = operators[i]
        if operator == "+":
            total = sum(nums)
            result += total
        else:
            base = 1
            for val in nums:
                base *= val
            result += base
        

print("Part One: ", result)

# Part 2
result = 0
chars = []

with open(fileName, "r") as file:
    for line in file:
        if len(chars) == 0:
            for char in line:
                chars.append([])
        for i in range(len(line)):
            chars[i].append(line[i])

    problems = []
    operators = []
    for column in chars:
        if column[0] == "\n":
            break
        if column[-1] == "+" or column[-1] == "*":
            operators.append(column[-1])
            problems.append([])
        problems[-1].append([])
        for val in column:
            if val != " " and val != "+" and val != "*":
                problems[-1][-1].append(val)

    for i in range(len(problems)):
        operator = operators[i]
        problemNums = problems[i]
        vals = []
        if i != len(problems)-1:
            problemNums = problemNums[:-1]
        for num in problemNums:
            sumNum = 0
            for j in range(len(num)):
                sumNum += int(num[j])*10**(len(num)-j-1)
            vals.append(sumNum)
        print(vals)
        print(operator)
        if operator == "+":
            total = sum(vals)
            print(total)
            result += total
        else:
            base = 1
            for val in vals:
                base *= val
            print(base)
            result += base

print("Part Two: ", result)