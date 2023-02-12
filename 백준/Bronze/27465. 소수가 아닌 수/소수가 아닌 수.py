from math import sqrt
n = int(input())
def p_n(x):
  while True:
    for i in range(2,int(sqrt(x))+1):
      if x % i == 0:
        return x
    x += 1
print(p_n(n))