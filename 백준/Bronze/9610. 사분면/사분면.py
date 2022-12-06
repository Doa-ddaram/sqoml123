import sys
axis, q1, q2, q3, q4 = 0, 0, 0, 0, 0
for i in range(0, int(sys.stdin.readline())):
  a, b = map(int, sys.stdin.readline().split())
  if a == 0 or b == 0:
    axis += 1
  elif a > 0 and b > 0:
    q1 += 1
  elif a > 0 and b < 0:
    q4 += 1
  elif a < 0 and b > 0:
    q2 += 1
  else:
    q3 += 1
print('Q1:',q1)
print('Q2:',q2)
print('Q3:',q3)
print('Q4:',q4)
print('AXIS:',axis)