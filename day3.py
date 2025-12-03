dayNum = "3"
simpleInput = True
fileName = "input"+dayNum+".txt" if simpleInput else "in.txt"

# Part 1

result = 0

with open(fileName, "r") as file:
    for line in file:
        first_num = 0
        second_num = -1
        print(line)
        for char in line[:-2]:
            if int(char) > second_num:
                second_num = int(char)
            if int(char) > first_num:
                first_num = int(char)
                second_num = -1
        if second_num == -1 or int(line[-2]) > second_num:
            second_num = int(line[-2])

        print(first_num, second_num)
        result += first_num*10 + second_num

print(result)

# Part 2

result = 0
with open(fileName, "r") as file:
    for line in file:
        line = line.strip()
        seqLen = 12
        nums = [0]*seqLen
        index = 0
        for char in line:
            charNum = int(char)
            posLeftToCheck = len(line) - index
            for i in range(seqLen-1, max(0, seqLen-posLeftToCheck)-1, -1):
                    if charNum > nums[i]:
                        nums[i] = charNum
                        for j in range(i+1, seqLen):
                            nums[j] = 0
            index += 1
            if index == len(line):
                break
        for i in range(seqLen):
            result += nums[i]*10**(seqLen-i-1)
        print(nums)
print(result)