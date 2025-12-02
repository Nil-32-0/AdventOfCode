import textwrap

dayNum = "2"

result = 0

with open("input2.txt", "r") as file:
    line = file.readline()
    splitline = line.split(",")
    for entry in splitline:
        entrysplit = entry.split("-")
        start = int(entrysplit[0])
        end = int(entrysplit[1])
        for i in range(start, end, 1):
            istr = str(i)
            invalid = False
            for j in range(1, len(istr)//2+1):
                if istr[:j] * (len(istr)//j) == istr:
                    invalid = True
            if invalid:
                result += i

print(result)