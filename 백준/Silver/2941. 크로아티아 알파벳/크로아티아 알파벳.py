import sys
input = sys.stdin.readline
t = input().rstrip()
total = 0
for i in range(len(t)-1):
  if t[i] == 'c':
    if t[i+1] == '=' or t[i+1] == '-':
      total += 1
  elif t[i] == 'd':
    if t[i+1] == '-':
      total += 1
    elif len(t) > 2:
      if (t[i+1] == 'z' and t[i+2] == '='):
        total += 1
  elif t[i] == 'l':
    if t[i+1] == 'j':
      total += 1
  elif t[i] == 'n':
    if t[i+1] == 'j':
      total += 1
  elif t[i] == 's':
    if t[i+1] == '=':
      total += 1
  elif t[i] == 'z':
    if t[i+1] == '=':
      total += 1
print(len(t)-total)