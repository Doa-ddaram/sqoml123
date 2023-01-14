import sys
input = sys.stdin.readline
n = int(input())
t_L = list(map(int,input().split()))
total_L = [t_L[0]]
Min = 0
for i in range(len(t_L)-1):
    if t_L[i] + 1 != t_L[i+1]:
        Min = t_L[i+1]
    if Min:
        total_L.append(Min)
        Min = 0
print(sum(total_L))