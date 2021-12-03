input = open("input-2021-2.txt", "r")
#print(input.read())

input = input.read().split("\n")
input.remove("")
#print(input[0].split(" "))

#PART-1
pos = 0
depth = 0

for instruction in input:
    parsed = instruction.split(" ")
    command = parsed[0]
    delta = parsed[1]
    if command == "forward":
        pos += int(delta)
    else:
        if command == "down":
            depth += int(delta)
        else:
            depth -= int(delta)

#print(pos)
#print(depth)
multiplied = (pos*depth)
print(multiplied)

#PART-2
pos = 0
depth = 0
aim = 0

for instruction in input:
    parsed = instruction.split(" ")
    command = parsed[0]
    delta = int(parsed[1])
    if command == "forward":
        pos += delta
        depth += (aim*delta)
    else:
        if command == "down":
            aim += delta
        else:
            aim -= delta

#print(pos)
#print(depth)
multiplied = (pos*depth)
print(multiplied)