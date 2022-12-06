import sys
sys.setrecursionlimit(10**6)


computer = int(input())
node = int(input())
sample_L = [[] for i in range(computer+1)]
check_L = [False for i in range(computer+1)]
for _ in range(node):
  a, b = map(int,input().split())
  sample_L[a].append(b)
  sample_L[b].append(a)
def DFS(x):
  global total
  check_L[x] = True
  total += 1
  for i in sample_L[x]:
    if check_L[i]:
        continue
    DFS(i)
total = 0
DFS(1)
print(total-1)