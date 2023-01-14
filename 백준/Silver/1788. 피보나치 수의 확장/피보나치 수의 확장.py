n = int(input())
if n == 0:
  print(0)
  print(0)
else:
  t = abs(n)
  if n > 0 or t % 2:
    print(1)
  else:
    print(-1)
  fiboabs_L = [0 for i in range(t+1)]
  fiboabs_L[1] = 1
  for i in range(2,t+1):
    fiboabs_L[i] = (fiboabs_L[i-1] % 1000000000) + (fiboabs_L[i-2] % 1000000000)
  print(fiboabs_L[t] % 1000000000)