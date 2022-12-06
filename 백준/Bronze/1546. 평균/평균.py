import sys
num = int(sys.stdin.readline())
L = list(map(int,sys.stdin.readline().split()))
Max = max(L)
for i in range(len(L)):
  L[i] = L[i] / Max * 100
print(sum(L)/len(L))