import sys
input  = sys.stdin.readline

n , m  = map(int, input().split())
s = []

def dfs():
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    
    for i in range(1, 1+n):
        if len(s)> 0:
            if s[-1] >= i:
                continue

        s.append(i)
        dfs()
        s.pop()

                
dfs()
