import sys
a = sys.stdin.readline().rstrip()
total = 0
sample_L = [['A','B','C'],['D','E','F'], ['G','H','I'], ['J','K','L'], ['M','N','O'],['P','Q','R','S'], ['T','U','V'],['W','X','Y','Z']]
for i in range(len(a)):
  for j in range(len(sample_L)):
    if sample_L[j].count(a[i]):
      t = j+3
  total += t
print(total)