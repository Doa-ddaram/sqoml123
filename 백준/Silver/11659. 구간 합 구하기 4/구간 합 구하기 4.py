import sys
input = sys.stdin.readline
M, N = map(int,input().split())
case_L = [0] + list(map(int,input().split()))
sum_L = [0 for i in range(M+1)]
for i in range(M):
    sum_L[i+1]= sum_L[i] + case_L[i+1]
for _ in range(N):
    a,b = map(int,input().split())
    print(sum_L[b] - sum_L[a-1])