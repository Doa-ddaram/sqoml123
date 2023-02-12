n = int(input())
print('YES')
if n % 4 == 1:
  for i in range(1,n,4):
    print(i,i+1,i+3,i+2, end = ' ')
  print(n)
elif n % 4 == 2:
  for i in range(1,n-4,4):
    print(i,i+1,i+3,i+2, end = ' ')
  print(n-1,n, end = ' ')
elif n % 4 == 3:
  for i in range(1,n-4,4):
    print(i+1,i,i+2,i+3, end = ' ')
  print(n-1,n-2,n,end = ' ')
else:
  for i in range(1, n+1, 4):
    print(i+1,i,i+2,i+3, end = ' ')