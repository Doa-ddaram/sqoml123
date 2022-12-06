import sys
from math import gcd
input = sys.stdin.readline
n, m = map(int,input().split())
t = m - n 
print(t // gcd(t, m), m // gcd(t,m))