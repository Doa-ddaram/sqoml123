import sys
n, m = map(int,sys.stdin.readline().split())
poket_dic = {}
for i in range(1,n+1):
  t = sys.stdin.readline().rstrip()
  poket_dic[i] = t
  poket_dic[t] = i
for _ in range(m):
  t = sys.stdin.readline().rstrip()
  if t.isdigit():
    print(poket_dic[int(t)])
  else:
    print(poket_dic[t])