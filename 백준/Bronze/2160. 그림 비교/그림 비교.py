# import pandas as pd
# t = pd.read_csv('/content/drive/MyDrive/ex1.csv')
import sys
input = sys.stdin.readline
n = int(input())
fin_L = []
pain_L = []
for i in range(n*5):
  pain_L.append(list(map(str,input().rstrip())))
for i in range(n-1):
  fir_L = pain_L[(5*i):(5*i+5)]
  total_L = []
  for j in range(i+1,n):
    sec_L = pain_L[(5*j):(5*j+5)]
    total = 0
    for r in range(5):
      for c in range(7):
        if fir_L[r][c] != sec_L[r][c]:
          total += 1
    total_L.append((total, i, j))
  total_L = sorted(total_L,key = lambda x : x[0])
  fin_L.append(total_L[0])
fin_L = sorted(fin_L, key = lambda x : x[0])
print((fin_L[0][1]+1),(fin_L[0][2]+1), sep = ' ')