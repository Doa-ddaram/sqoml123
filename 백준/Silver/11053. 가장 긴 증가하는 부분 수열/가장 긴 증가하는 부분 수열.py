case_L = []
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
t_L = [0]
for i in range(len(c_L)):
  t = len(t_L)
  temp = bi(0, t-1,c_L[i])
  if temp >= t:
    t_L.append(c_L[i])
  else:
    t_L[temp] = c_L[i]
print(len(t_L)-1)