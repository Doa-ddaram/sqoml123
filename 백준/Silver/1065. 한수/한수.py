import sys
input = sys.stdin.readline
n = int(input())

def hansu(x):
  if x < 10:
    return 1
  else:
    x = list(map(int,str(x)))
    t = x[0] - x[1]
    for i in range(len(x)-1):
      if t != x[i]- x[i+1]:
        return 0
    return 1
total = 0
for i in range(1,n+1):
  total = total + hansu(i)
print(total)