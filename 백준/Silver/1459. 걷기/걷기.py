import sys
X,Y,W,S = map(int,input().split())
if W > S:
  if abs(X-Y) % 2:
    total = (min(X,Y) * S) + (abs(X-Y) - 1) * S + W
  else:
    total = max(X,Y) * S
elif 2 * W < S:
  total = (X + Y) * W
else:
  total = min(X,Y) * S + abs(X-Y) * W
print(total)