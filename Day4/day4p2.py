f = open("input.txt", "r")
lines = f.readlines()
numberlist = []
count = 0
for line in lines:
    nums = line.replace('-', ' ')
    nums = nums.replace('\n', '')
    nums = nums.replace(',', ' ')
    pos = nums.split()
    if (int(pos[0]) < int(pos[2]) and int(pos[1]) < int(pos[2])) or (int(pos[0]) > int(pos[3]) and int(pos[1]) > int(pos[3])):
        print(pos)
        count += 1
print(len(lines) - count)
f.close()