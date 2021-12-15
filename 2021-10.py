import timeit
import re
input = open("input-2021-10.txt", "r")
input = input.read().split("\n")

illegals = []
incomplete = []

def foo(l):
    stop = False
    while stop == False:
        for i,elem in enumerate(l):
            if elem == ')':
                if l[i-1] == '(':
                    l.pop(i)
                    l.pop(i-1)
                    #print(l)
                elif l[i-1] in ['(','[','{','<']:
                    #print('Illegal')
                    illegals.append(l[i])
                    stop = True
                    break
            elif elem == ']':
                if l[i-1] == '[':
                    l.pop(i)
                    l.pop(i-1)
                    #print(l)
                elif l[i-1] in ['(','[','{','<']:
                    #print('Illegal')
                    illegals.append(l[i])
                    stop = True
                    break
            elif elem == '}':
                if l[i-1] == '{':
                    l.pop(i)
                    l.pop(i-1)
                    #print(l)
                elif l[i-1] in ['(','[','{','<']:
                    #print('Illegal')
                    illegals.append(l[i])
                    stop = True
                    break
            elif elem == '>':
                if l[i-1] == '<':
                    l.pop(i)
                    l.pop(i-1)
                    #print(l)
                elif l[i-1] in ['(','[','{','<']:
                    #print('Illegal')
                    illegals.append(l[i])
                    stop = True
                    break
        if (']' not in l) and ('}' not in l) and (')' not in l) and ('>' not in l):
            stop = True
    if (']' not in l) and ('}' not in l) and (')' not in l) and ('>' not in l):
        incomplete.append(l)
    return(l)

starttime = timeit.default_timer()

#PART-1

for line in input:
    foo(list(line))
error = 0
for illegal in illegals:
    if illegal == ')':
        error +=3
    if illegal == ']':
        error +=57
    if illegal == '}':
        error +=1197
    if illegal == '>':
        error +=25137
print(error)
print("The time difference is :", timeit.default_timer() - starttime)
starttime = timeit.default_timer()

#PART-2
scores = []

for line in incomplete:
    score = 0
    closers = line
    closers.reverse()
    for elem in closers:
        if elem == '(':
            score*=5
            score+=1
        elif elem == '[':
            score*=5
            score+=2
        elif elem == '{':
            score*=5
            score+=3
        elif elem == '<':
            score*=5
            score+=4
    scores.append(score)
scores.sort()
print(scores[int(len(scores)/2)])
print("The time difference is :", timeit.default_timer() - starttime)