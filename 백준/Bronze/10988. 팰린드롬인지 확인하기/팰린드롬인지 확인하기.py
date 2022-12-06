import sys
a = input()
t = 0
for i in range(0, len(a)//2):
  if a[i] != a[i * -1 -1]:
    t += 1
    break
if t != 0:
  print(0)
else:
  print(1)