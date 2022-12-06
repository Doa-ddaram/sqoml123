import sys
n = int(sys.stdin.readline())
atm_L = list(map(int,input().split()))
atm_L.sort()
total = 0
for i in range(n):
  total += sum(atm_L[:i+1])
print(total)