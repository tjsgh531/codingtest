import sys
input = sys.stdin.readline

def nqueen(row):
    if row == N-1:
        result += 1
        return
    
    for i in range(N):
        if check(row, i):
            board[row][i] = 1
            nqueen(row+1)
            board[row][i] = 0

def check(row, col):
    #1 같은 열(col)에 있는가
    for i in range(row-1):
        if board[i][col] == 1:
            return False
    #2 대각선에 있는가
    for i in range(row-1):
        gap = row - i
        # 왼쪽 대각선
        if col - gap > 0:
            if board[i][col-gap] == 1:
                return False
        # 오른쪽 대각선    
        if col + gap < N:
            if board[i][col+gap] == 1:
                return False
    return True

if __name__ == 'main':
    N = int(input())
    result = 0
    board = [[0]* N]*N
    nqueen(0)