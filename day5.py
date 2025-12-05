def __main__():
    dayNum = "5"
    fullInput = True
    fileName = "input"+dayNum+".txt" if fullInput else "in.txt"

    # Part 1

    result = 0
    fresh = []
    parseFresh = True

    with open(fileName, "r") as file:
        for line in file:
            line = line.strip()
            if not parseFresh:
                val = int(line)
                for start, end in fresh:
                    if start <= val <= end:
                        result += 1
                        break
            if line == "":
                parseFresh = False
            if parseFresh:
                vals = line.split("-")
                fresh.append((int(vals[0]), int(vals[1])))

    print("Part One: ", result)

    # Part 2
    result = 0

    with open(fileName, "r") as file:
        fresh.sort(key=lambda item: item[0])
        cur = fresh[0]
        newFresh = []
        for next in fresh[1:]:
            if cur[1] >= next[0]:
                if next[1] > cur[1]:
                    cur = (cur[0], next[1])
            else:
                newFresh.append(cur)
                cur = next
        newFresh.append(cur)
        fresh = newFresh
        for start, end in fresh:
            result += end-start+1
    print("Part Two: ", result)
    # 318140662027902
    # 355555479253787

__main__()