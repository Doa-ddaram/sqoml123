import sys
notcu, cu = 0, 0
for i in range(0, int(sys.stdin.readline())):
  a = int(input())
  if a == 0:
    notcu += 1
  else:
    cu += 1
if notcu > cu:
  print('Junhee is not cute!')
else:
  print('Junhee is cute!')