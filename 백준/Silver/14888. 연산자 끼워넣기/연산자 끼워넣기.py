from itertools import permutations
import sys
n = int(input())
case_L = list(map(int,input().split()))
pl,mi,mu,di = map(int,input().split())
operator_L = [1] * pl + [2] * mi + [3] * mu + [4] * di
real_L = list(permutations(operator_L,n-1))
total_L = []
for i in range(len(real_L)):
  temp = case_L[0]
  for j in range(n-1):
    if real_L[i][j] == 1:
      temp = temp + case_L[j+1]
    elif real_L[i][j] == 2:
      temp = temp - case_L[j+1]
    elif real_L[i][j] == 3:
      temp = temp * case_L[j+1]
    elif real_L[i][j] == 4:
      if temp < 0:
        temp *= -1
        temp = temp // case_L[j+1]
        temp *= -1
      else:
        temp = temp // case_L[j+1]
  total_L.append(temp)
total_L.sort()
print(total_L[-1])
print(total_L[0])