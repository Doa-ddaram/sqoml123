import sys
input = sys.stdin.readline
n = int(input())
Str= sys.stdin.readline().rstrip()
total = 0
for i in range(n):
  total = total + (((ord(Str[i])-96) * (31 ** i)) % 1234567891)
print(total % 1234567891)