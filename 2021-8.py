import timeit
input = open("input-2021-8.txt", "r")
input = input.read().split("\n")

starttime = timeit.default_timer()

count = 0

for line in input:
    line = line.split(" ")
    output = line[11:15]
    #print(output)
    for digit in output:
        if len(digit) == 2 or len(digit) == 4 or len(digit) == 3 or len(digit) == 7:
            count+=1

print(count)

print("The time difference is :", timeit.default_timer() - starttime)
starttime = timeit.default_timer()

sum = 0
i = 1

for line in input:
    line = line.split(" ")
    input = line[0:10]
    output = line[11:15]
    num = ""
    key = {}
    for digit in input:
        if len(digit) == 2:
            key["1"] = digit
        elif len(digit) == 4: 
            key["4"] = digit
        elif len(digit) == 3: 
            key["7"] = digit
        elif len(digit) == 7:
            key["8"] = digit

    #print(key)

    for digit in input:
        if len(digit) == 5:#5/2/3
            if set(key["1"]).intersection(set(digit)) == set(key["1"]):
                key["3"] = digit
            else:
                if len(set(key["4"]).intersection(set(digit))) == 3:
                    key["5"] = digit
                else:
                    key["2"] = digit
        if len(digit) == 6:#6/9/0
            if len(set(key["1"]).intersection(set(digit))) == 1:
                key["6"] = digit
            else:
                if len(set(key["4"]).intersection(set(digit))) == 4:
                    key["9"] = digit
                else:
                    key["0"] = digit
            
    #print(key)
    for digit in output:
        for x in key:
            if set(key[x]) == set(digit):
                num += x

    #print("i: "+str(i))
    num = int(num)
    #print(num)
    sum+=num
    num = ""
    i+=1

print(sum)

print("The time difference is :", timeit.default_timer() - starttime)