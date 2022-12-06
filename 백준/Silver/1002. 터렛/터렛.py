import sys
from math import sqrt
for _ in range(int(input())):
  turret_L = list(map(int, input().split()))
  dist = sqrt((turret_L[0] - turret_L[3]) ** 2 + (turret_L[1] - turret_L[4]) ** 2)
  if dist > turret_L[2] and dist > turret_L[5]:
    if dist > turret_L[2] + turret_L[5]:
      print(0)
    elif dist < turret_L[2] + turret_L[5]:
      print(2)
    else:
      print(1)
  elif dist == 0:
    if turret_L[2] == turret_L[5]:
      print(-1)
    else:
      print(0)
  else:
    if abs(turret_L[2] - turret_L[5]) - dist > 0:
      print(0)
    elif abs(turret_L[2] - turret_L[5]) - dist < 0:
      print(2)
    else:
      print(1)