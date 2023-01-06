from collections import deque
import sys
input = sys.stdin.readline
D = deque()
def pu_b(x):
  D.appendleft(x)
def pu_f(x):
  D.append(x)
def pop_b():
  if D:
    t = D.popleft()
    print(t)
  else:
    print(-1)
def pop_f():
  if D:
    t = D.pop()
    print(t)
  else:
    print(-1)
for i in range(int(input())):
  T = input().rstrip()
  if T[:2] == 'pu':
    if T[5] == 'b':
      pu_b(T[10:])
    else:
      pu_f(T[11:])
  elif T[:2] == 'po':
    if T[4] == 'b':
      pop_b()
    else:
      pop_f()
  elif T[:2] == 'si':
    print(len(D))
  elif T[:2] == 'em' :
    if D:
      print(0)
    else:
      print(1)
  elif T[:2] == 'fr':
    if D:
      print(D[-1])
    else:
      print(-1)
  else:
    if D:
      print(D[0])
    else:
      print(-1)