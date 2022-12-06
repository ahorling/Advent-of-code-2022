f = open("input.txt", "r")
line = f.read()
i = 0
x = 0
while x != 4:
    unique_chars = set(line[i : i + 4])
    x = len(unique_chars)
    i += 1
    ret = i + 4 - 1

print(ret)