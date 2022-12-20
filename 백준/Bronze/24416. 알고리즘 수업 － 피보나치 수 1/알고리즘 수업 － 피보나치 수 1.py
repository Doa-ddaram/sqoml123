import sys
n = int(input())
code1_L = [0, 1,1,2,3,5]+[0] * 35
code2_L = [0,0,0]+list(range(1,n-1))
for i in range(6,n+1):
  code1_L[i] = code1_L[i-1]+code1_L[i-2]
print(code1_L[n], code2_L[n])