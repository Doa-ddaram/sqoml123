import sys
input = sys.stdin.readline
for _ in range(int(input())):
  x,y = map(int,input().split())
  temp = y - x
  if temp <= 2:
    print(temp)
    continue
  for i in range(0,2**16):
    st = i ** 2 + i+1
    en = i ** 2 + 3 * i + 2
    if st <= temp <= en:
      if temp - st < en - temp:
        t = 2 * i +1
      else:
        t = 2 * i + 2
      break
  print(t)