import sys
n = input()
t = 1
for i in range(len(n) - 1):
  if n[i] == n[i+1]:
    t += 1
  else:
    break
print(t)