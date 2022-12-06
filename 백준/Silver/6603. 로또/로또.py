from itertools import combinations
while True:
  case_L = list(map(int,input().split()))
  if len(case_L) == 1:
    break
  a = case_L[0]
  case_L = case_L[1:]
  t = list(combinations(case_L, 6))
  for i in range(len(t)):
    for j in range(6):
      print(t[i][j], end = ' ')
    print()
  print()