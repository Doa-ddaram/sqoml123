L = []
for _ in range(7):
    I = int(input())
    if I % 2:
        L.append(I)
L.sort()
if len(L):
    print(sum(L))
    print(L[0])
else:
    print(-1)
    