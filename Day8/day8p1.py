f = open("input.txt", "r")
lines = f.read().splitlines()
f.close()

count = 0
grid = [[int(num) for num in line] for line in lines]
treegrid = [[0 for x in range(len(lines))] for y in range(len(lines[0]))]
for y in range(len(grid)):
    tallesttree = -1
    for x in range(len(grid[0])):
        if tallesttree == 9:
            break
        if grid[y][x] > tallesttree:
            tallesttree = grid[y][x]
            treegrid[y][x] = 1

for y in range(len(grid) - 1, -1, -1):
    tallesttree = -1
    for x in range(len(grid[0]) - 1, -1, -1):
        if tallesttree == 9:
            break
        if grid[y][x] > tallesttree:
            tallesttree = grid[y][x]
            treegrid[y][x] = 1

for x in range(len(grid[0])):
    tallesttree = -1
    for y in range(len(grid)):
        if tallesttree == 9:
            break
        if grid[y][x] > tallesttree:
            tallesttree = grid[y][x]
            treegrid[y][x] = 1

for x in range(len(grid[0]) - 1, -1, -1):
    tallesttree = -1
    for y in range(len(grid) -1, -1, -1):
        if tallesttree == 9:
            break
        if grid[y][x] > tallesttree:
            tallesttree = grid[y][x]
            treegrid[y][x] = 1

for line in treegrid:
    for tree in line:
        if tree == 1:
            count += 1
print(count)