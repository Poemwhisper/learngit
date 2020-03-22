board_opening = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def print_board(bo,bo_op):
    if bo == bo_op:
        print('problem cannot be solved!')
    else:
        for i in range(9): 
            if i%3 == 0 and i != 0:
                print('---------------------')
            for j in range(9):
                if j == 8:
                    print(str(bo[i][j]))
                elif j%3 == 0 and j != 0:
                    print('| '+str(bo[i][j])+' ', end='')
                else:
                    print(str(bo[i][j])+' ', end='')

def check_solve(bo):
    if find_empty(bo) == None:
        return True
    else:
        return False

def do_solve(bo):
    pos = find_empty(bo)
    print('Now searching the answer for ' + '(' + str(pos[0]) + ',' + str(pos[1]) + '):')

    for i in range(1,10):
        print('checking '+str(i)+' for '+'(' + str(pos[0]) + ',' + str(pos[1]) + ')!')
        if check_valid(bo, i, pos) == True:
            bo[pos[0]][pos[1]] = i
            print(str(i)+ ' is a temperarily right answer for ' + '(' + str(pos[0]) + ',' + str(pos[1]) + ')!')
    
            if check_solve(bo) != True:
                do_solve(bo)
                if check_solve(bo) == True:
                    return True

            else:
                print('problem solved!')
                return True

            bo[pos[0]][pos[1]] = 0

    print('Nothing fit in here! Go back!')
    return False

def find_empty(bo):
    for i in range(9):
        for j in range(9):
            if bo[i][j] == 0:
                return (i,j)
    return None

def check_valid(bo, num, pos):
    #check column
    for i in range(9):
        if num == bo[i][pos[1]] and i != pos[0]:
            return False
    #check row
    for j in range(9):
        if num == bo[pos[0]][j] and j != pos[1]:
            return False
    #check box
    for i in range((pos[0]//3)*3,(pos[0]//3)*3+3):
        for j in range((pos[1]//3)*3,(pos[1]//3)*3+3):
            if num == bo[i][j] and (i,j) != pos:
                return False

    return True

do_solve(board)
print_board(board, board_opening)
