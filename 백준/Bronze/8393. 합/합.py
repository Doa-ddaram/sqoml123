N = int(input())
l = N
inp = 0
for i in range(0,l):
    if N == 0:
        break
    inp += N
    N -= 1
print(inp)