import sys                                      #10093번 완성본
a, b = map(int,input().split())
if b > a :
  print(b-a-1)
  total_L = []
  for i in range(a+1,b):
    total_L.append(i)
  print(' '.join(map(str,total_L)))
elif a > b:
  print(a-b-1)
  total_L = []
  for i in range(b+1,a):
    total_L.append(i)
  print(' '.join(map(str,total_L)))
else:
  print(0)