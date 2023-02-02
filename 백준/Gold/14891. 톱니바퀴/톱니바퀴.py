from collections import deque                     #14891번 완성본
import sys
input = sys.stdin.readline
gear_q = [deque()]
gear_L = list(deque(map(int,input().rstrip())) for _ in range(4))
gear_q = gear_q + gear_L
K = int(input())
for _ in range(K):
  n, dir = map(int,input().split())
  if n == 1:
    if gear_q[n][2] != gear_q[n+1][6]:
      if gear_q[n+1][2] != gear_q[n+2][6]:
        if gear_q[n+2][2] != gear_q[n+3][6]:
          if dir == 1:
            gear_q[n].rotate(1)
            gear_q[n+1].rotate(-1)
            gear_q[n+2].rotate(1)
            gear_q[n+3].rotate(-1)
          else:
            gear_q[n].rotate(-1)
            gear_q[n+1].rotate(1)
            gear_q[n+2].rotate(-1)
            gear_q[n+3].rotate(1)
        else:
          if dir == 1:
            gear_q[n].rotate(1)
            gear_q[n+1].rotate(-1)
            gear_q[n+2].rotate(1)
          else:
            gear_q[n].rotate(-1)
            gear_q[n+1].rotate(1)
            gear_q[n+2].rotate(-1)
      else:
        if dir == 1:
          gear_q[n].rotate(1)
          gear_q[n+1].rotate(-1)
        else:
          gear_q[n].rotate(-1)
          gear_q[n+1].rotate(1) 
    else:
      if dir == 1:
        gear_q[n].rotate(1)
      else:
        gear_q[n].rotate(-1)
  elif n == 2:
    if gear_q[n][6] != gear_q[n-1][2]:
      if dir == 1:
        gear_q[n-1].rotate(-1)
      else:
        gear_q[n-1].rotate(1)
    if gear_q[n][2] != gear_q[n+1][6]:
      if gear_q[n+1][2] != gear_q[n+2][6]:
        if dir == 1:
          gear_q[n].rotate(1)
          gear_q[n+1].rotate(-1) 
          gear_q[n+2].rotate(1)
        else:
          gear_q[n].rotate(-1)
          gear_q[n+1].rotate(1)
          gear_q[n+2].rotate(-1) 
      else:
        if dir == 1:
          gear_q[n].rotate(1)
          gear_q[n+1].rotate(-1)
        else:
          gear_q[n].rotate(-1)
          gear_q[n+1].rotate(1)
    else:
      if dir == 1:
        gear_q[n].rotate(1)
      else:
        gear_q[n].rotate(-1) 
  elif n == 3:
    if gear_q[n][2] != gear_q[n+1][6]:
      if dir == 1:
        gear_q[n+1].rotate(-1)
      else:
        gear_q[n+1].rotate(1) 
    if gear_q[n][6] != gear_q[n-1][2]:
      if gear_q[n-1][6] != gear_q[n-2][2]:
        if dir == 1:
          gear_q[n].rotate(1)
          gear_q[n-1].rotate(-1)
          gear_q[n-2].rotate(1)
        else:
          gear_q[n].rotate(-1)
          gear_q[n-1].rotate(1)
          gear_q[n-2].rotate(-1)
      else:
        if dir == 1:
          gear_q[n].rotate(1)
          gear_q[n-1].rotate(-1)
        else:
          gear_q[n].rotate(-1)
          gear_q[n-1].rotate(1)
    else:
      if dir == 1:
        gear_q[n].rotate(1)
      else:
        gear_q[n].rotate(-1) 
  else:
    if gear_q[n][6] != gear_q[n-1][2]:
      if gear_q[n-1][6] != gear_q[n-2][2]:
        if gear_q[n-2][6] != gear_q[n-3][2]:
          if dir == 1:
            gear_q[n].rotate(1)
            gear_q[n-1].rotate(-1)
            gear_q[n-2].rotate(1)
            gear_q[n-3].rotate(-1)
          else:
            gear_q[n].rotate(-1)
            gear_q[n-1].rotate(1)
            gear_q[n-2].rotate(-1)
            gear_q[n-3].rotate(1)
        else:
          if dir == 1:
            gear_q[n].rotate(1)
            gear_q[n-1].rotate(-1)
            gear_q[n-2].rotate(1)
          else:
            gear_q[n].rotate(-1)
            gear_q[n-1].rotate(1)
            gear_q[n-2].rotate(-1)
      else:
        if dir == 1:
          gear_q[n].rotate(1)
          gear_q[n-1].rotate(-1)
        else:
          gear_q[n].rotate(-1)
          gear_q[n-1].rotate(1) 
    else:
      if dir == 1:
        gear_q[n].rotate(1)
      else:
        gear_q[n].rotate(-1)

print(gear_q[1][0] + gear_q[2][0] * 2 + gear_q[3][0] * 4 + gear_q[4][0] * 8)