from math import factorial
import sys
N, K = map(int,input().split())
print(factorial(N) // (factorial(K)* factorial(N-K)))