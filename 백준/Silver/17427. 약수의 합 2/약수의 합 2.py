import sys
a = int(input())
total = 0
for i in range(1, a+1):
  total = total + i * (a // i)
print(total) 