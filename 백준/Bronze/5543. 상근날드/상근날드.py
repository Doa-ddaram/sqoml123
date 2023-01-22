h_L,b_L=[],[]
import sys
input = sys.stdin.readline
for i in range(3):
    h_L.append(int(input()))
h_L.sort()
for i in range(2):
    b_L.append(int(input()))
b_L.sort()
print(h_L[0] + b_L[0] - 50)