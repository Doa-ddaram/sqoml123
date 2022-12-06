from math import lcm
import sys
for i in range(0, int(sys.stdin.readline())):
    a, b = map(int, sys.stdin.readline().split())
    print(lcm(a,b))