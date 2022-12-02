# A = Rock
# B = Paper
# C = Sissors
# X = Lose
# Y = Draw
# Z = Win

def chosen(char1, char2):
    if (char1 == 'A' and char2 == 'X'):
        return 3
    if (char1 == 'A' and char2 == 'Y'):
        return 1
    if (char1 == 'A' and char2 == 'Z'):
        return 2
    if (char1 == 'B' and char2 == 'X'):
        return 1
    if (char1 == 'B' and char2 == 'Y'):
        return 2
    if (char1 == 'B' and char2 == 'Z'):
        return 3
    if (char1 == 'C' and char2 == 'X'):
        return 2
    if (char1 == 'C' and char2 == 'Y'):
        return 3
    if (char1 == 'C' and char2 == 'Z'):
        return 1

f = open("input.txt", "r")
lines = f.readlines()
score = 0
for line in lines:
    if (line[2] == 'X'):
        score += 0
    if (line[2] == 'Y'):
        score += 3
    if (line[2] == 'Z'):
        score += 6
    score += chosen(line[0], line[2])
print(score)