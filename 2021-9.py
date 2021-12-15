import timeit
input = open("input-2021-9.txt", "r")
input = input.read().split("\n")

starttime = timeit.default_timer()

input = [[int(x) for x in line] for line in input]
risk = 0
low_points = []

#PART-1

for row,line in enumerate(input):
    for col,num in enumerate(line):
        x = input[row][col]
        if col-1 < 0:
            left = 9
        else:
            left = input[row][col-1]
        if col+1 < 0:
            right = 9
        else:
            try:
                right = input[row][col+1]
            except:
                right = 9
        if row-1 < 0:
            up = 9
        else:
            up = input[row-1][col]
        if row+1 < 0:
            down = 9
        else:
            try:
                down = input[row+1][col]
            except:
                down = 9
        if x<left and x<right and x<up and x<down:
            risk+=x+1
            low_points.append([row,col])
    else:
        continue
    break
print(risk)
print("The time difference is :", timeit.default_timer() - starttime)
starttime = timeit.default_timer()

#PART-2

basins = []

def checknearby(row,col):
    global size
    for delta in [[0,-1],[0,1],[-1,0],[1,0]]:
        dr = delta[0]
        dc = delta[1]
        if [row+dr,col+dc] not in seen and row+dr>-1 and col+dc>-1 and row+dr<len(input) and col+dc<len(input[0]):
            seen.append([row+dr,col+dc])
            if input[row+dr][col+dc] < 9:
                queue.append([row+dr,col+dc])
                size+=1

for point in low_points:
    seen = [point]
    queue = [point]
    size = 1
    while len(queue) > 0:
        row = queue[0][0]
        col = queue[0][1]
        checknearby(row,col)
        queue.remove(queue[0])
        #print(queue)
    basins.append(size)

basins.sort(reverse=True)
mul = basins[0]*basins[1]*basins[2]
print(mul)
print("The time difference is :", timeit.default_timer() - starttime)