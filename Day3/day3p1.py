f = open("input.txt", "r")
lines = f.readlines()
sum = 0
for line in lines:
    compartment1 = slice(0,len(line)//2)
    compartment2 = slice(len(line)//2, len(line))
    for ch in line[compartment1]:
        if ch in line[compartment2]:
            print(ch)
            if ord(ch) >= 97 and ord(ch) <= 122:
                sum += ord(ch) - 96
            if ord(ch) >= 65 and ord(ch) <= 90:
                sum += ord(ch) - 38
            break
print(sum)
