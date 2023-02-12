n, m = map(int,input().split())
S = list(map(str,input()))
from collections import deque
pr_q = deque()
for i in range(len(S)-1,-1,-1):
  if S[i] != 'A' and S[i] != 'E' and S[i] != 'I' and S[i] != 'O' and S[i] != 'U':
    pr_q.append(S[i])
    temp = i
    break
if len(pr_q) == 0:
  print('NO')
else:
  for i in range(temp-1, -1, -1):
    if len(pr_q) == 3:
      temp = i + 1
      break
    if S[i] == 'A':
      pr_q.appendleft(S[i])
  if len(pr_q) != 3:
    print('NO')
  else:
    if temp - (m - 3) >= 0:
      print('YES')
      for i in range(temp-(m-4)):
        print(S[i] , end = '')
      for i in range(3):
        print(pr_q[i], end = '')
    else:
      print('NO')