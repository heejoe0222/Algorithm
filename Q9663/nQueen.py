global N, result
result=0

def printBoard(board):
    global result
    '''
    for i in range(N):
        for j in range(N):
            print (board[i][j], end=' ')
        print()
    print()
    '''
    result+=1

def promising(board, row, col):
    #같은 열에 있는지 검사
    for i in range(col):
        if board[row][i] == 1:
            return False
    #왼쪽으로 위쪽 대각선 검사
    for i,j in zip(range(row,-1,-1), range(col,-1,-1)):
        if board[i][j] == 1:
            return False

    #왼쪽으로 아래쪽 대각선 검사
    for i,j in zip(range(row,N,1), range(col,-1,-1)):
        if board[i][j] == 1:
            return False

    return True

def queens(board, col):
    if col == N:
        printBoard(board)
        return True

    flag = False
    for i in range(N):
        if promising(board, i, col):
            board[i][col] = 1

            flag = queens(board, col+1) or flag
            board[i][col] = 0

    return flag

def solveNQueen(N):
    board = [ [0]*N for i in range(N) ]

    if queens(board, 0) == False:
        print ("Solution does not exist")
        return
    return

N = int(input())
solveNQueen(N)
print(result)
