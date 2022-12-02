# A + X = Rock
# B + Y = Paper
# C + Z = Sissors

def winorlose(char1, char2):
    if (char1 == 'A' and char2 == 'Y'):
        return 1
    if (char1 == 'A' and char2 == 'Z'):
        return 0
    if (char1 == 'B' and char2 == 'X'):
        return 0
    if (char1 == 'B' and char2 == 'Z'):
        return 1
    if (char1 == 'C' and char2 == 'X'):
        return 1
    if (char1 == 'C' and char2 == 'Y'):
        return 0
    else:
        return 2

f = open("input.txt", "r")
lines = f.readlines()
score = 0
for line in lines:
    if (line[2] == 'X'):
        score += 1
    if (line[2] == 'Y'):
        score += 2
    if (line[2] == 'Z'):
        score += 3
    if (winorlose(line[0], line[2]) == 1):
        score += 6
    if (winorlose(line[0], line[2]) == 2):
        score += 3
print(score)