n = int(input())
def sum3():
  ex_L = [[0,1,2],[0,1,3],[0,3,4],[0,2,4],[5,1,2],[5,1,3],[5,3,4],[5,2,4]]
  min_L = []
  for i in range(8):
    p,q,r = ex_L[i][0],ex_L[i][1],ex_L[i][2] 
    min_L.append(dice_L[p]+dice_L[q]+dice_L[r])
  return min(min_L)
def sum2():
  ex_L = [[0,1],[0,2],[0,3],[0,4],[1,5],[2,5],[3,5],[4,5],[2,1],[3,1],[4,2],[3,4]]
  min_L = []
  for i in range(12):
    p,q = ex_L[i][0],ex_L[i][1]
    min_L.append(dice_L[p]+dice_L[q])
  return min(min_L)
def sum1():
  ex_L = sorted(dice_L)
  return ex_L[0]
if n == 1:
  dice_L = list(map(int,input().split()))
  dice_L.sort()
  print(sum(dice_L[:5]))
elif n == 2:
  dice_L = list(map(int,input().split()))
  sum3 = sum3()
  sum2 = sum2()
  print(4 * sum3 + 4 * sum2)
else:
  dice_L = list(map(int,input().split()))
  sum3 = sum3()
  sum2 = sum2()
  sum1 = sum1()
  print(4 * sum3 + (2 * n - 3) * 4 * sum2 + ((n-2) * (5 * n - 6) * sum1))