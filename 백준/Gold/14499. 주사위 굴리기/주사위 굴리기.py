import sys

n, m, x, y, order = map(int,sys.stdin.readline().split())
map_L = [[0 for i in range(m)] for j in range(n)]
for i in range(n):
  map_L[i] = list(map(int,sys.stdin.readline().split()))
dice_L = [0 for i in range(6)]
order_L = list(map(int,sys.stdin.readline().split()))
for i in range(order):
  if order_L[i] == 1:
    y += 1
    if x >= n or y >= m or x < 0 or y < 0:
      y -= 1
      continue
    dice_L[0],dice_L[1],dice_L[2],dice_L[3],dice_L[4],dice_L[5] = dice_L[0],dice_L[5],dice_L[1],dice_L[2],dice_L[4],dice_L[3]
  elif order_L[i] == 2:
    y -= 1
    if x >= n or y >= m or x < 0 or y < 0:
      y += 1
      continue
    dice_L[0],dice_L[1],dice_L[2],dice_L[3],dice_L[4],dice_L[5] = dice_L[0],dice_L[2],dice_L[3],dice_L[5],dice_L[4],dice_L[1]
  elif order_L[i] == 3:
    x -= 1
    if x >= n or y >= m or x < 0 or y < 0:
      x += 1
      continue
    dice_L[0],dice_L[1],dice_L[2],dice_L[3],dice_L[4],dice_L[5] = dice_L[2],dice_L[1],dice_L[4],dice_L[3],dice_L[5],dice_L[0]
  elif order_L[i] == 4:
    x += 1
    if x >= n or y >= m or x < 0 or y < 0:
      x -= 1
      continue
    dice_L[0],dice_L[1],dice_L[2],dice_L[3],dice_L[4],dice_L[5] = dice_L[5],dice_L[1],dice_L[0],dice_L[3],dice_L[2],dice_L[4]
  if map_L[x][y] == 0:
    map_L[x][y] = dice_L[5]
  elif map_L[x][y] != 0:
    dice_L[5] = map_L[x][y]
    map_L[x][y] = 0
  print(dice_L[2])