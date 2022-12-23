import sys
R,C = map(int,sys.stdin.readline().split())
bread_L = [list(map(str,sys.stdin.readline().rstrip())) for i in range(R)]
nx = [-1,0,1]
def dfs(x,y):
  bread_L[x][y] = 'x'
  if y == C-1:
    return True
  for i in range(3):
    dx = x + nx[i]
    if 0 <= dx < R and bread_L[dx][y+1] == '.':
        if dfs(dx, y+1):
          return True
  return False
total = 0
for i in range(R):
  if dfs(i,0):
    total += 1
print(total)