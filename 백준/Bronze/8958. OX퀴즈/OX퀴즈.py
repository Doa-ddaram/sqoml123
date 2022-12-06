import sys
for i in range(0, int(input())):
  total, temp = 0, 0
  t = list(input())
  if t[0] == 'O':
    total += 1
    temp += 1
  for j in range(0, len(t)-1):
    if t[j] == 'O' and t[j+1] == 'O':
      temp += 1
    elif t[j] == 'O' and t[j+1] == 'X':
      temp = 0
    elif t[j] == 'X' and t[j+1] == 'O':
      temp += 1
    total += temp
  print(total)