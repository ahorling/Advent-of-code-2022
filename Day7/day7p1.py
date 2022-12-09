f = open("input.txt", "r")
lines = f.read().splitlines()
f.close()
dictbranch = {}
pwd = []
for line in lines:
    data = line.split(' ')
    if data[1] == "cd":
        if data[2] == "/":
            pwd.append(data[2])
            dictbranch[data[2]] = 0
        elif data[2] == "..":
            pwd.pop(len(pwd) - 1)
        else:
            pwd.append(pwd[-1] + data[2] + '/')
    elif data[0] == "dir":
        if pwd[-1] + data[1] not in dictbranch:
            dictbranch[pwd[-1] + data[1] + '/'] = 0
    elif data[0].isdigit():
        for dir in pwd:
            dictbranch[dir] += int(data[0])
for k, v in dictbranch.items():
    print(k, v)
size = 0
for dir in dictbranch:
    if dictbranch[dir] <= 100000:
        size += dictbranch[dir]
print(size)

