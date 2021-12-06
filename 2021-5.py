input = open("input-2021-5.txt", "r")
#print(input.read())

input = input.read().split("\n")
input.remove("")

input = [x.split(" -> ") for x in input]
input = [[x.split(',') for x in sublist] for sublist in input]
input = [[[int(x) for x in xy] for xy in pair] for pair in input]

#print(input)

max = 0
for line in input:
    for pair in line:
        for num in pair:
            #print(num)
            if num > max:
                #print(num)
                max = num

rows, cols = (max, max)
arr = [[0 for i in range(cols+1)] for j in range(rows+1)]
# for row in arr:
#     print(row)

def parse1(x1,y1,x2,y2):
    #print(f"{x1},{y1} {x2},{y2}")
    global arr
    if x1 == x2:
        #print(f"{x1},{y1} {x2},{y2}")
        if y2>y1:
            for x in range(y1,y2+1):
                arr[x][x1]+=1
        else:
            for x in reversed(range(y2,y1+1)):
                arr[x][x1]+=1
                
    elif y1 == y2:
        #print(f"{x1},{y1} {x2},{y2}")
        if x2>x1:
            for x in range(x1,x2+1):
                arr[y1][x]+=1
        else:
            for x in reversed(range(x2,x1+1)):
                arr[y1][x]+=1

for line in input:
    parse1(line[0][0],line[0][1],line[1][0],line[1][1])

# for row in arr:
#     print(row)

count = 0
for row in arr:
    for num in row:
        if num > 1:
            count+=1
print(count)

arr = [[0 for i in range(cols+1)] for j in range(rows+1)]

diagonal_points=[]

def parse2(x1,y1,x2,y2):
    #print(f"{x1},{y1} {x2},{y2}")
    global arr
    if x1 == x2:
        #print(f"{x1},{y1} {x2},{y2}")
        if y2>y1:
            for x in range(y1,y2+1):
                arr[x][x1]+=1
        else:
            for x in reversed(range(y2,y1+1)):
                arr[x][x1]+=1
                
    elif y1 == y2:
        #print(f"{x1},{y1} {x2},{y2}")
        if x2>x1:
            for x in range(x1,x2+1):
                arr[y1][x]+=1
        else:
            for x in reversed(range(x2,x1+1)):
                arr[y1][x]+=1
    else:
        #print(f"{x1},{y1} {x2},{y2}")
        global diagonal_points
        deltax = x2-x1
        deltay = y2-y1
        x=x1
        y=y1
        diagonal_points.append([x,y])
        gradient = deltay/deltax
        #print("Gradient = "+str(gradient))
        if gradient == 1:
            for i in range(abs(deltax)):
                if y2<y1 and x2<x1:
                    x-=1
                    y-=1
                elif y2>y1 and x2>x1:
                    x+=1
                    y+=1
                #print([x,y])
                diagonal_points.append([x,y])
        elif gradient == -1:
            for i in range(abs(deltax)):
                if y2>y1 and x2<x1:
                    x-=1
                    y+=1
                elif y2<y1 and x2>x1:
                    x+=1
                    y-=1
                else:
                    print("ERROR")
                #print([x,y])
                diagonal_points.append([x,y])
        else:
            print("ERROR")

for line in input:
    parse2(line[0][0],line[0][1],line[1][0],line[1][1])

#print(diagonal_points)

for point in diagonal_points:
    arr[point[1]][point[0]] += 1

# for row in arr:
#     print(row)

count = 0
for row in arr:
    for num in row:
        if num > 1:
            count+=1
print(count)

