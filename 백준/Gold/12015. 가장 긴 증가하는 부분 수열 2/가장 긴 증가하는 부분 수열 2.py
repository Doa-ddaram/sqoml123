import sys
input = sys.stdin.readline
case_L = []
def binary(sta,end,x):
    while sta<=end:
        m = (sta+end)//2
        if temp_L[m] >= x:
            end = m - 1
        else:
            sta = m + 1
    return sta
n = int(input())
case_L = list(map(int,input().split()))
temp_L = [0]
for i in range(len(case_L)):
  t = len(temp_L)
  temp = binary(0, t-1,case_L[i])
  if temp == t:
    temp_L.append(case_L[i])
  temp_L[temp] = case_L[i]
print(len(temp_L)-1)