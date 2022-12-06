ori_L = [1,1,2,2,2,8]
case_L = list(map(int,input().split()))
for i in range(6):
  print(ori_L[i] - case_L[i],end = ' ')