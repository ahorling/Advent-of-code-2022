f = open("input.txt", "r")
lines = f.read().splitlines()
f.close

def move_left(grid, distance, posH, posT):
    i = 0
    while i < distance:
        posH[0] = posH[0] - 1
        if abs(posH[0] - posT[0]) > 1:
            posT[0] = posT[0] - 1
            posT[1] = posH[1]
            grid[posT[1]][posT[0]] = "#"
        i += 1
        # print(posH)


def move_right(grid, distance, posH, posT):
    i = 0
    while i < distance:
        posH[0] = posH[0] + 1
        if abs(posH[0] - posT[0]) > 1:
            posT[0] = posT[0] + 1
            posT[1] = posH[1]
            grid[posT[1]][posT[0]] = "#"
        i += 1
        # print(posH)

def move_up(grid, distance, posH, posT):
    i = 0
    while i < distance:
        posH[1] = posH[1] + 1
        if abs(posH[1] - posT[1]) > 1:
            posT[1] = posT[1] + 1
            posT[0] = posH[0]
            grid[posT[1]][posT[0]] = "#"
        i += 1
        # print(posH)

def move_down(grid, distance, posH, posT):
    i = 0
    while i < distance:
        posH[1] = posH[1] - 1
        if abs(posH[1] - posT[1]) > 1:
            posT[1] = posT[1] - 1
            posT[0] = posH[0]
            grid[posT[1]][posT[0]] = "#"
        i += 1
        # print(posH)



grid = [["." for x in range(300)] for y in range(300)]
x = 149
y = 0
posH = [x,y]
posT = [x,y]

for line in lines:
    instructions = line.split(' ')
    if instructions[0] == "R":
        move_right(grid, int(instructions[1]), posH, posT)
    elif instructions[0] == "L":
        move_left(grid, int(instructions[1]), posH, posT)
    elif instructions[0] == "U":
        move_up(grid, int(instructions[1]), posH, posT)
    elif instructions[0] == "D":
        move_down(grid, int(instructions[1]), posH, posT)

count = 1
for row in grid:
    for ch in row:
        if ch == "#":
            count += 1
print(count)

visualize = []
for row in grid:
    visualize.append(' '.join(str(r) for r in row))
print('\n'.join(visualize))


