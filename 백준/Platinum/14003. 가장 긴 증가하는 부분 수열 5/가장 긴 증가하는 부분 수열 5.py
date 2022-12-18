import os, io
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
def bi(st,en,x):
    while st<=en:
        m = (st+en)//2
        if t_L[m] >= x:
            en = m - 1
        else:
            st = m + 1
    return st
n = int(input())
c_L = list(map(int,input().split()))
t_L = [c_L[0]]
q_L = []
for i in range(len(c_L)):
  t = len(t_L)
  temp = bi(0, t-1,c_L[i])
  if temp == t:
    t_L.append(c_L[i])
    q_L.append((len(t_L)-1,c_L[i]))
  else:
    t_L[temp] = c_L[i]
    q_L.append((temp,c_L[i]))
print(len(t_L))
p=len(t_L)-1

total_L=[]
for i in range(n-1,-1,-1):
    if q_L[i][0]==p:
        total_L.append(q_L[i][1])
        p-=1
for i in range(len(total_L)-1,-1,-1):
  print(total_L[i], end = ' ')