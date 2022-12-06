from math import factorial as fact
n,m = map(int,input().split())
print(fact(n)//(fact(m)*fact(n-m)))