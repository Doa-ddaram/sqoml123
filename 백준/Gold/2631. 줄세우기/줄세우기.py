import sys
case_L = []
def binary(sta,end,x):
    while sta<=end:
        m = (sta+end)//2
        if temp_L[m] >= x:
            end = m - 1
        else:
            sta = m + 1
    return sta
for i in range(int(sys.stdin.readline())):
  case_L.append(int(sys.stdin.readline()))
temp_L = [0]
for i in range(len(case_L)):
  temp = binary(0,len(temp_L)-1,case_L[i])
  if temp == len(temp_L):
    temp_L = temp_L + [0]
  temp_L[temp] = case_L[i]
print(len(case_L) - (len(temp_L)-1))