import sys
input = sys.stdin.readline
t = list(map(str,input().rstrip()))
if sum(map(int,t)) % 3:
  print(-1)
else:
  t.sort(reverse = 1)
  if t[-1] == '0':
    for i in t:
      print(i,end='')
  else:
    print(-1)