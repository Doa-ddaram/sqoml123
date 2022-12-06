t = 0
while True:
  t += 1
  n = int(input())
  if n == 0:
    break
  if n % 2 == 0:
    print('%d. even %d' %(t, n // 2))
  else:
    print('%d. odd %d' %(t, (n - 1) // 2))