n = int(input())        #2417번
def bi(x,y,m):
  while x <= y:
    t = (x+y) // 2
    if t ** 2 >= m:
      y = t-1
    else:
      x = t+1
  return x
print(bi(0,2**32,n))