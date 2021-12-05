input = open("input-2021-4.txt", "r")
#print(input.read())

input = input.read().split("\n")
random_nums = input[0].split(",")
input.remove(input[0])
boards = [x for x in input if x != '' and x != ' ']
for i,line in enumerate(boards):
    boards[i]=([x for x in (boards[i].split(" ")) if x != ''])

boards = [boards[x:x+5] for x in range(0,len(boards),5)] #format boards

def check_rows(input):
    for n,board in enumerate(input):
        for line in board:
            if all(x == line[0] for x in line):
                print("Bingo!")
                return n

def check_columns(input):
    for n,board in enumerate(input):
        for i,column in enumerate(board[0]):
            column = [row[i] for row in board]
            if all(x == column[0] for x in column):
                print("Bingo!")
                return n

def check_diagonals(input):
    for n,board in enumerate(input):
        i,j=0,0
        diagonal = []
        for x in range(len(board)):
            diagonal.append(board[i][j])
            i+=1
            j+=1
        if all(x == diagonal[0] for x in diagonal):
            return n
        i,j=0,4
        diagonal = []
        for x in range(len(board)):
            diagonal.append(board[i][j])
            i+=1
            j-=1
        if all(x == diagonal[0] for x in diagonal):
            return n

def check(input):
    if check_rows(boards) != None:
        return check_rows(boards)
    elif check_columns(boards) != None:
        return check_columns(boards)
    # elif check_diagonals(boards) != None:
    #     return check_diagonals(boards)
    else:
        return False



#print(boards)

def fun():
    for num in random_nums:
        for n,board in enumerate(boards):
            for i,line in enumerate(board):
                for j,x in enumerate(line):
                    if x == num:
                        boards[n][i][j] = 'X'
                        if check_rows(boards) != None:
                            result = boards[n]
                            return check_rows(boards),result,num
                        if check_columns(boards) != None:
                            result = boards[n]
                            return check_columns(boards),result,num
                        # if check_diagonals(boards) != None:
                        #     result = boards[n]
                        #     return check_diagonals(boards),result

def sum(board):
    sum = 0
    for row in board:
        for x in row:
            if x != 'X':
                sum += int(x)
    return sum

#PART-1
# board,result,num = fun()
# print(sum(result)*int(num))

#PART-2
while len(boards) > 1:
    board,result,num = fun()
    boards.remove(result)

board, result,num = fun()                
print(sum(result)*int(num))


            