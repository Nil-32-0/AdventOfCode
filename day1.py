num = 50
cnt = 0

def tickRight():
    global num
    global cnt
    num += 1
    if num > 99:
        num = 0
        cnt += 1

def tickLeft():
    global num
    global cnt
    num -= 1
    if num == 0:
        cnt += 1
    if num < 0:
        num = 99

with open("input1.txt", "r") as file:
    for line in file:
        print(line)
        for i in range(int(line[1:])):
            if line[0] == "L":
                tickLeft()
            else:
                tickRight()

print(cnt)