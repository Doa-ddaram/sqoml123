import sys                        #14503번 완성본
input = sys.stdin.readline
N, M = map(int,input().split())
r,c, d = map(int,input().split())
case_L = [list(map(int,input().split())) for i in range(N)]
cl_L = [] 
cl_L.append([r,c,d])
co = 0
def clean():
  global co
  d_x = [0,1,0,-1,-1,0,1,0,0,-1,0,1,1,0,-1,0]
  d_y = [-1,0,1,0,0,-1,0,1,1,0,-1,0,0,1,0,-1]
  while cl_L:
    t = cl_L.pop()
    X,Y = t[0],t[1]
    d = t[2]
    if case_L[X][Y] == 0:
      case_L[X][Y] = 3
      co += 1
    temp = 0
    for i in range(4*d,4*d+4):
      temp += 1
      dx = X + d_x[i]
      dy = Y + d_y[i]
      if case_L[dx][dy] == 0 :
        temp = 0
        if d_x[i] == 0:
          if d_y[i] == 1:
            d = 1
          else:
            d = 3
        elif d_y[i] == 0:
          if d_x[i] == 1:
            d = 2
          else:
            d = 0
        cl_L.append([dx,dy,d])
        case_L[dx][dy] = 3
        co += 1
        break
    if temp == 4:
      if d == 1 or d == 3:
        d_d = 4-d
      else:
        d_d = 2-d
      temp_L = [[-1,0],[0,1],[1,0],[0,-1]]
      if case_L[X+temp_L[d_d][0]][Y+temp_L[d_d][1]] == 1:
        return
      else:
        cl_L.append([X+temp_L[d_d][0],Y+temp_L[d_d][1],d])
clean()
print(co)
