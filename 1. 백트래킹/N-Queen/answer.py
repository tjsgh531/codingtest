''' ---------------- 정답 예시1 ---------------- '''
n = int(input())

ans = 0
row = [0] * n

def is_promising(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            return False
    
    return True

def n_queens(x):
    global ans
    if x == n:
        ans += 1
        return

    else:
        for i in range(n):
            # [x, i]에 퀸을 놓겠다.
            row[x] = i
            if is_promising(x):
                n_queens(x+1)

n_queens(0)
print(ans)

''' ---------------- 정답 예시2 ---------------- '''

def nqueen(depth):     
  global result
  
  # depth가 N일 때 > 모든 퀸을 다 놓은 것
  if depth == N : 
    result += 1 
    return 

  # depth별 반복문 
  for i in range(N):

    # 해당 depth를 visited 하지 않았을 때 
    if visited[i] == False : 
      board[depth] = i     # (depth, i)에 퀸 올리기 (여기서 depth는 raw, i는 column에 해당
      
      if check(depth):
        visited[i] = True
        nqueen(depth + 1)     # 그 다음 열로 넘어감 
        visited[i] = False    # 다시 false로 설정해 백트래킹 


# 모든 열에대해 퀸과 대각선, 좌우에 위치해 있는지 체크 
def check(n):
  for i in range(n):

    # 좌우에 있거나, 대각선에 있다면 
    # TODO(여기서 기존 queen이 어떻게 적재되고 있는걸까?)
    if (board[n] == board[i]) or (n-i == abs(board[n] - board[i])):
      return False

  return True

# main 
if __name__ == '__main__':
  N = int(input())    # dfs의 depth에 해당함 
  # depth별 적재 
  board = [0] * N     # 1차원 리스트로 적재 
  visited = [False] * N
  result = 0 

  nqueen(0)
  print(result)
