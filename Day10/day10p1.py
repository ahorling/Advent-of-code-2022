f = open("input.txt", "r")
lines = f.read().splitlines()
f.close()


def check_cycles(cycles, i, count):
    if cycles == 20 or (cycles == (20 + 40 * i) and cycles < 221):
        count = count + (cycles * x)
        print(cycles * x)
        i += 1
        return (i, count)
    return (i, count)

cycles = 0
x = 1
i = 0
count = 0
for line in lines:
    line = line.split(' ')
    if line[0] == "noop":
        cycles += 1
        i, count = check_cycles(cycles, i, count)
    if line[0] == "addx":
        cycles += 1
        i, count = check_cycles(cycles, i, count)
        x += int(line[1])
        cycles += 1
        i, count = check_cycles(cycles, i, count)
print("final sum is: " + str(count))



