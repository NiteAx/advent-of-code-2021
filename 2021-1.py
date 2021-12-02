input = open("input-2021-1.txt", "r")
#print(input.read())

depths = input.read().split('\n')
depths.remove("") #clean input
size_of_depths = len(depths)

# print(depths)
# print(size_of_depths)

#PART-1
inc = 0
prev = int(depths[0])

for depth in depths:
    if int(depth) > prev:
        inc+=1
    prev = int(depth)

print(inc)

#PART-2
inc = 0
prev = 0

for idx,depth in enumerate(depths):
    try:
        a = int(depths[idx])
        b = int(depths[idx+1])
        c = int(depths[idx+2])
    except:
        break
    #print(str(a)+" "+str(b)+" "+str(c))
    sum = a+b+c
    if sum > prev and idx > 0:
        inc+=1
    prev = sum

print(inc)
