import sys
input = sys.stdin.readline
S = input().rstrip()
t = 0
for i in range(len(S)):
    if S[i] == ':':
        t += 2
    elif S[i] == '_':
        t += 6
    else:
        t += 1
print(t)