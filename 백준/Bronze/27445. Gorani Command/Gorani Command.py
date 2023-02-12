a,b = map(int,input().split())
Min = (60,0)
for i in range(a-1):
  t = int(input())
  if Min[0] > t:
    Min = (t,i+1)
r = Min[1]
last_L = list(map(int,input().split()))
if last_L[0] < Min[0]:
  Min = (last_L[0], a)
  r = a
print(r,Min[0] + 1)