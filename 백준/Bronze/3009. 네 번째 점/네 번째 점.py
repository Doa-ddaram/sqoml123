L1, L2 = [],[]
for i in range(0,3):
  a, b = map(int, input().split())
  L1.append(a)
  L2.append(b)
if L1[0] == L1[1]:
  if L2[0] == L2[1] :
    print(L1[2], L2[2])
  elif L2[0] == L2[2]:
    print(L1[2], L2[1])
  else:
    print(L1[2], L2[0])
elif L1[0] == L1[2]:
  if L2[0] == L2[1] :
    print(L1[1], L2[2])
  elif L2[0] == L2[2]:
    print(L1[1], L2[1])
  else:
    print(L1[1], L2[0])
else:
  if L2[0] == L2[1] :
    print(L1[0], L2[2])
  elif L2[0] == L2[2]:
    print(L1[0], L2[1])
  else:
    print(L1[0], L2[0])