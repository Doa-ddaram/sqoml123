import sys
a, b = map(int,sys.stdin.readline().split())
A, B = a, b
while a % b != 0 and b % a != 0:
  if a > b:
    temp = a - b
    a = temp
  else:
    temp = b - a
    b = temp
print(min(a, b))
print(A * B // min(a,b))