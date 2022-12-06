import sys
while True:
  per = []
  t = int(sys.stdin.readline())
  if t == -1:
    break
  for i in range(1, t // 2 + 1):
    if t % i == 0:
      per.append(i)
  if sum(per) == t:
    print("%d =" %(t),' + '.join(map(str, per)))
  else:
    print("%d is NOT perfect." %t)