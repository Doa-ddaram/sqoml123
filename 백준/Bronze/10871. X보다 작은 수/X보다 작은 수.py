n, k = map(int,input().split())
L = list(map(int,input().split()))
for i in range(n):
    if L[i] < k:
        print(L[i], end = ' ')