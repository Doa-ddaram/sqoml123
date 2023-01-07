# 2 ** 19 == 524288
n = int(input())
for i in range(19):
  if 2 ** i <= n < 2 ** (i+1):
    t = 2 ** i
    break
if t == n:
  print(n)
elif n == 1:
  print(1)
else:  
  print((n - t) * 2)