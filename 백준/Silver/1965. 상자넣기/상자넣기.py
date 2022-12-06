import sys
box_L = []
def binary(sta,end,x):
    while sta<=end:
        m = (sta+end)//2
        if temp_L[m] >= x:
            end = m - 1
        else:
            sta = m + 1
    return sta
N = int(sys.stdin.readline())
box_L = list(map(int,sys.stdin.readline().split()))
temp_L = [0]
for i in range(len(box_L)):
  temp = binary(0,len(temp_L)-1,box_L[i])
  if temp == len(temp_L):
    temp_L = temp_L + [0]
  temp_L[temp] = box_L[i]
print(len(temp_L)-1)