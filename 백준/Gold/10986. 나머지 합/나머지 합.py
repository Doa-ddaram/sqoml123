import sys
input = sys.stdin.readline
N, M = map(int,input().split())                 
ori_L = [0] + list(map(int,input().split()))
Len = len(ori_L)
cal_L = [0 for _ in range(Len)]
group_L = [0 for i in range(M)]
for i in range(1,Len):
  cal_L[i] = (cal_L[i-1] + ori_L[i]) % M
  group_L[cal_L[i]] += 1
total = group_L[0]
for i in range(M):
  k = group_L[i]
  total = total + (k * (k - 1) // 2)
print(total)