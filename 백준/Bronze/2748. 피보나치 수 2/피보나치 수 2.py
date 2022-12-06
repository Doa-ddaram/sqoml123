import sys
Pibo = [0,1] + [1] * 90
for i in range(2,91):
  Pibo[i] = Pibo[i-1] + Pibo[i-2]
N = int(sys.stdin.readline())
print(Pibo[N])