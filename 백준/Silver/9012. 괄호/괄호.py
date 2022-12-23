for _ in range(int(input())):
  cs = input()
  paren_L = [0] * 50
  for i in range(len(cs)):
    if cs[i] == '(':
      paren_L.append(3)
    else:
      paren_L.pop()
  if len(paren_L) == 50 and paren_L.count(3) == 0:
    print('YES')
  else:
    print('NO')