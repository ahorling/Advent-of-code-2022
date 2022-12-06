f = open("input.txt", "r")
line = f.read()
i = 0
x = 0
while x != 14:
    unique_chars = set(line[i : i + 14])
    x = len(unique_chars)
    i += 1
    ret = i + 14 - 1

print(ret)