n, r = map(int,input().split())
big = 10 ** 9 + 7
A = 1
B = 1
for i in range(1,n+1):
  A = A * i
  A = A % big
for i in range(1,r+1):
  B = B * i
  B = B % big
for i in range(1,n-r+1):
  B = B * i
  B = B % big
def divpow(a,m):
  temp = 1
  while m > 0:
    if m % 2 != 0:
      temp = temp * a
      temp = temp % big
    a = a * a
    a = a % big
    m = m // 2
  return temp        
t = divpow(B,big-2) % big
temp = t*A
temp = temp % big 
print(temp)