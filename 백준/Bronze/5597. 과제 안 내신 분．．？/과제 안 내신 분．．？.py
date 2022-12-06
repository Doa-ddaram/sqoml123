import sys
sample_L = list(range(1,31))
for _ in range(28):
  n = int(sys.stdin.readline())
  sample_L.remove(n)
for i in range(len(sample_L)):
  print(sample_L[i])