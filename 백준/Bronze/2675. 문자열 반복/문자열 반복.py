import sys
for i in range(0, int(sys.stdin.readline())):
    a, b = map(list, input().split())
    a = int(a[0])
    for _ in b:
      print(_ * a, end = '')
    print("")