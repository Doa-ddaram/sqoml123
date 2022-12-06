A, B = map(int,input().split())
C = int(input())
A += (B + C) // 60
if A >= 24:
  print((A-24), ((B+C)%60))
else : 
  print(A, (B+C) % 60)