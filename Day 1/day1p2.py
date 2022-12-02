f = open("input.txt", "r")
lines = f.readlines()
calories = 0
calories1 = 0
calories2 = 0
calories3 = 0
for line in lines:
    if (line.strip() != ""):
        calories = calories + int(line)
    else:
        if (calories > calories1):
            calories3 = calories2
            calories2 = calories1
            calories1 = calories
        if (calories > calories2 and calories < calories1):
            calories3 = calories2
            calories2 = calories
        if (calories > calories3 and calories < calories2):
            calories3 = calories
        calories = 0
print(calories1 + calories2 + calories3)
