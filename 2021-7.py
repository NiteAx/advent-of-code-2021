import timeit

input = open("input-2021-7.txt", "r")
input = input.read().split(",")
#print(input)
input = [int(x) for x in input]

starttime = timeit.default_timer()
#print("The start time is :",starttime)

minfuel = 10000000000000000000000

for e in range(min(input), max(input)+1):
    fuel = 0
    for pos in input:
        fuel+=abs(int(pos)-int(e))
    #print(fuel)
    if fuel < minfuel:
        minfuel = fuel

print(minfuel)

print("The time difference is :", timeit.default_timer() - starttime)
starttime = timeit.default_timer()

minfuel = 10000000000000000000000

j=0

for e in range(min(input), max(input)+1):
    j+=1
    fuel = 0
    for pos in input:
        df = 0
        for i in range(abs(pos-e)):
            df+=1
            fuel+=df
    if fuel < minfuel:
        minfuel = fuel
    #print(j)

print(minfuel)
print("The time difference is :", timeit.default_timer() - starttime)