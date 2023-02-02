import sys
input = sys.stdin.readline
n = int(input())    #1744번 완성본
pos_L,neg_L = [],[]
one, zero,tot = 0,0,0
for _ in range(n):
  t = int(input())
  if t > 1:
    pos_L.append(t)
  elif t == 1:
    one += 1
  elif t == 0:
    zero += 1
  else:
    neg_L.append(t)
pos_L.sort(reverse = True)
neg_L.sort()
Ln = len(neg_L) 
Lp = len(pos_L)
if Lp:
  for i in range(0,Lp-1,2):
    tot = tot + pos_L[i] * pos_L[i+1]
  if Lp % 2:
    tot += pos_L[-1]
if Ln:
  for i in range(0,Ln-1,2):
    tot = tot + neg_L[i] * neg_L[i+1]
  if Ln % 2 and zero == 0:
    tot += neg_L[-1]
print(tot + one)