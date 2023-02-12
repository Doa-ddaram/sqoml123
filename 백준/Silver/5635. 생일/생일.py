import sys
input = sys.stdin.readline
n = int(input())
tset_L = [list(map(str, input().split())) for i in range(n)]
Max = [tset_L[0][0],int(tset_L[0][1]),int(tset_L[0][2]),int(tset_L[0][3])]
Min = [tset_L[0][0],int(tset_L[0][1]),int(tset_L[0][2]),int(tset_L[0][3])]
for i in range(n):
  t0 = tset_L[i][0]
  t1,t2,t3 = int(tset_L[i][1]),int(tset_L[i][2]),int(tset_L[i][3])
  if t3 > Min[3]:
    Min = [t0,t1,t2,t3]
  elif t3 == Min[3]:
    if t2 > Min[2]:
      Min = [t0,t1,t2,t3]
    elif t2 == Min[2]:
      if t1 > Min[1]:
        Min = [t0,t1,t2,t3]
  if t3 < Max[3]:
    Max = [t0,t1,t2,t3]
  elif t3 == Max[3]:
    if t2 < Max[2]:
      Max = [t0,t1,t2,t3]
    elif t2 == Max[2]:
      if t1 < Max[1]:
        Max = [t0,t1,t2,t3]
print(Min[0])
print(Max[0])