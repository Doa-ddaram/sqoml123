import sys
input = sys.stdin.readline
N = int(input())
IQ_L = list(map(int,input().split()))
if N == 1:
  print('A')
elif N >= 3:
  if IQ_L[2] == IQ_L[1] or IQ_L[0] == IQ_L[1]:
    a = 0
    b = IQ_L[2]
    check = False
    for i in range(1,N):
      if IQ_L[i] != b:
        check = True
        print('B')
        break
    if check == False:
      print(b)
  else:
    a = (IQ_L[2] - IQ_L[1]) / (IQ_L[1] - IQ_L[0])
    if int(a) != a:
      print('B')
    else:
      a = int(a)
      b = IQ_L[1] - IQ_L[0] * a
      check = False
      for i in range(0,N-1):
        if IQ_L[i] * a + b != IQ_L[i+1]:
          check = True
          print('B')
          break
      if check == False:
        print(IQ_L[-1] * a + b)
else:
  if IQ_L[0] == IQ_L[1]:
    print(IQ_L[0])
  else:
    print('A')