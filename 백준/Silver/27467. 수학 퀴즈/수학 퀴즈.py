N = input()
case_L = list(map(int,input().split()))
p, q = 0.0, 0.0
for i in range(len(case_L)):
  if case_L[i] == 0 or case_L[i] % 3 == 0:
    q += 1.0
  elif case_L[i] % 3 == 1:
    p += 1.0
  else:
    p -= 1.0
    q -= 1.0
print('%.6lf %.6lf' %(p,q))