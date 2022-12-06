import sys        #완성본 1476번 (해결책이 떠오름)
a, b, c = map(int, input().split())
A, B, C = a, b, c
while True:
  if A == B == C:
    print(A)
    break
  if A > 7980 :
    print(-1)
    break
  if A - b < 0 :
    A += 15
  if (A - b) % 28 == 0:
    if (A - c) % 19 == 0:
      print(A)
      break
    else:
      A += 15
  else:
    A += 15