import sys
for _ in range(0, int(sys.stdin.readline())):
  dic = dict() 
  N = int(sys.stdin.readline())
  for i in range(N):
    a, b = map(str, sys.stdin.readline().split())
    b = int(b)
    dic[b] = a
  dic = sorted(dic.items(), key = None, reverse = True)
  print(dic[0][1])