def d(x):
  t = str(x)
  total = x
  for i in t:
    total += int(i)
  return total
L = set()
for i in range(1,9973):
  L.add(d(i))
for i in range(1,10001):
  if i not in L:
    print(i)