import sys
input = sys.stdin.readline
def prime_list(n):
    sieve_L = [True] * n
    from math import sqrt as s
    m = int(s(n))
    for i in range(2, m + 1):
        if sieve_L[i] == True:           
            for j in range(i+i, n, i): 
                sieve_L[j] = False
    return [i for i in range(2, n) if sieve_L[i] == True]
L = prime_list(1000000)
S_L = set(L)
def ju():
  for i in range(len(L)):
    if n-L[i] in S_L:
      return (n, L[i], n-L[i])
while True:
  n = int(input())
  if n == 0:
    break
  t = ju()
  print('%d = %d + %d'%(t[0],t[1],t[2]))
