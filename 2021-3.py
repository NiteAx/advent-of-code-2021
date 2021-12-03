input = open("input-2021-3.txt", "r")
#print(input.read())

input = input.read().split("\n")
input.remove("")
#print(input)

#PART-1
gamma = ""
epsilon = ""
#power = gamma*epsilon

a=[[] for i in range(len(input[0]))]

for num in input:
    num = list(num)
    i=0
    for digit in num:
        a[i].append(int(digit))
        i+=1

def most_frequent(List):
    counter = 0
    num = List[0]
     
    for i in List:
        curr_frequency = List.count(i)
        if(curr_frequency> counter):
            counter = curr_frequency
            num = i
 
    return num

def flip(Str):
    output = ""
    for digit in list(Str):
        if digit == "0":
            output+="1"
        else:
            output+="0"
    return output

for sublist in a:
    gamma += str(most_frequent(sublist))

epsilon = flip(gamma)
gamma = int(gamma,2)
epsilon = int(epsilon,2)
print(gamma*epsilon)

o2gen = 0
co2scrub = 0

i=0
one = 0
zero = 0
temp = input
for x in range(len(input[0])):
    for num in input:
        if num.startswith("1",i):
            one += 1
        if num.startswith("0",i):
            zero += 1

    if one > zero:
        #print("1 wins")
        input = [x for x in input if x.startswith("1",i)]
    elif one < zero:
        #print("0 wins")
        input = [x for x in input if x.startswith("0",i)]
    else:
        #print("=")
        input = [x for x in input if x.startswith("1",i)]
    #print(input)
    i+=1
    one=0
    zero=0
    if len(input) < 2:
        break

o2gen = int(input[0],2)
#print(o2gen)
input=temp
i=0

for x in range(len(input[0])):
    for num in input:
        if num.startswith("1",i):
            one += 1
        if num.startswith("0",i):
            zero += 1

    if one > zero:
        #print("1 wins")
        input = [x for x in input if x.startswith("0",i)]
    elif one < zero:
        #print("0 wins")
        input = [x for x in input if x.startswith("1",i)]
    else:
        #print("=")
        input = [x for x in input if x.startswith("0",i)]
    #print(input)
    i+=1
    one=0
    zero=0
    if len(input) < 2:
        break
    
co2scrub = int(input[0],2)
lifesupport = o2gen*co2scrub
print(lifesupport)