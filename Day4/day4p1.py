f = open("input.txt", "r")
lines = f.readlines()
numberlist = []
count = 0
for line in lines:
    nums = line.replace('-', ' ')
    nums = nums.replace('\n', '')
    nums = nums.replace(',', ' ')
    pos = nums.split()
    if (int(pos[2]) <= int(pos[0]) and int(pos[3]) >= int(pos[1])) or (int(pos[2]) >= int(pos[0]) and int(pos[3]) <= int(pos[1])):
        print(pos)
        count += 1
print(count)
f.close()
