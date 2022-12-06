def make_stacks(lines):
    stacks = [[]]

    i = 0
    while (i < 8):
        i += 1
        stacks.append([])

    for line in lines:
        if line[0] is '[':
            i = 0
            while i * 4 + 1 <= 35:
                if line[i * 4 + 1] is not ' ':
                    stacks[i].insert(0, line[i * 4 + 1])
                i += 1
        else:
            break
    return stacks



f = open("input.txt", "r")
lines = f.read().splitlines()
stacks = make_stacks(lines)
i = 0
for line in lines[10:]:
    splitline = line.split(' ')
    i = int(splitline[1])
    movefrom = int(splitline[3]) - 1
    moveto = int(splitline[5]) - 1
    while i > 0:
        moved = stacks[movefrom].pop(len(stacks[movefrom]) - i)
        stacks[moveto].append(moved)
        i -= 1

print[stacks]
