def create_groups(list, wanted_parts):
    length = len(list)
    return [ list[i*length // wanted_parts: (i+1)*length // wanted_parts]
            for i in range(wanted_parts) ]

f = open("input.txt", "r")
lines = f.readlines()
lines[:] = [line.strip() for line in lines]
sum = 0
groups = create_groups(lines, len(lines)/3)
for group in groups:
    badge = str(set.intersection(*map(set, group)))
    badge = badge[6]
    print(badge)
    if ord(badge) >= 97 and ord(badge) <= 122:
        sum += ord(badge) - 96
    if ord(badge) >= 65 and ord(badge) <= 90:
        sum += ord(badge) - 38
print(sum)