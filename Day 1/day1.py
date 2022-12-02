f = open("input.txt", "r")
lines = f.readlines()
calories = 0
maxcalories = 0
for line in lines:
    if (line.strip() != ""):
        calories = calories + int(line)
    else:
        if (calories >= maxcalories):
            maxcalories = calories
        calories = 0
print(maxcalories)
