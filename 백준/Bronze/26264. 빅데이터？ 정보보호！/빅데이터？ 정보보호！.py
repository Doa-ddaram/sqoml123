n = int(input())
Len = len(input())
big = 8 * n - Len
sec = Len - 7 * n
if big > sec:
  print('bigdata?')
elif big < sec:
  print('security!')
else:
  print('bigdata? security!')