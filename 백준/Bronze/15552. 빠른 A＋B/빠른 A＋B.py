import sys
def add(a, b):
    return a + b
n = int(sys.stdin.readline())
for i in range(0,n):
    A, B = map(int, sys.stdin.readline().split())
    print(add(A,B))