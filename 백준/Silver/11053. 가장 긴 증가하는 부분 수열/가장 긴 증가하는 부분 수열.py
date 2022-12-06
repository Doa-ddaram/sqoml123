import sys                                        #11053번 미완성본
size = int(sys.stdin.readline())
inc_L = [0]+ list(map(int,input().split()))
check_L = [0 for i in range(size+1)]
for i in range(1,size+1):
  if i == 1:
    check_L[i] = 1
    continue
  Max = 1
  for j in range(1,i):
    if inc_L[j] < inc_L[i] and Max <= check_L[j]: 
      Max = check_L[j] + 1
  check_L[i] = Max
print(max(check_L))