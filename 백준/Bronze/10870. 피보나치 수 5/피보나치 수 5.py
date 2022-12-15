import sys
fibo_L = [0,1,1] + [0 for i in range(18)]
for i in range(1,19):
    fibo_L[i+2] = fibo_L[i+1] + fibo_L[i]
n = int(input())
print(fibo_L[n])