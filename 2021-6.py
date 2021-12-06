from collections import Counter

input = open("input-2021-6.txt", "r")
input = input.read().split(",")
#print(input)

fishes = input
fishes = [int(fish) for fish in fishes]
day = 0
addfish = 0

#print(fishes)

for day in range(80):
    fishes = [fish-1 if fish>0 else 6 for fish in fishes]
    for count in range(addfish):
        fishes.append(8)
    addfish = 0
    day+=1
    for fish in fishes:
        if fish == 0:
            addfish += 1
        
    #print(f"{fishes} {addfish}")
    #print(f"{len(fishes)}")

print(len(fishes))

fishes = input
fishes = [int(fish) for fish in fishes]
fishes = Counter(fishes)
#print(fishes)

for day in range(256):
    newfeesh = fishes[0]
    for x in range(8):
        fishes[x] = fishes[x+1]
    fishes[8] = newfeesh
    fishes[6] += newfeesh
    #print(sum(fishes.values()))

print(sum(fishes.values()))
    