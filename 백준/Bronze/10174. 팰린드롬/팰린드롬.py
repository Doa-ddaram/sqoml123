import sys
# input = sys.stdin.readline
n = int(input())
def Fal(x):
    for i in range(len(x)//2):
        if x[i] != x[-1-i]:
            return 'No'
    return 'Yes'
for _ in range(n):
    S = input()
    print(Fal(S.lower()))

        