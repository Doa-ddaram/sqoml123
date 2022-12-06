from string import ascii_lowercase

alp_L = list(ascii_lowercase)
L = input()
total_L = [-1] * len(alp_L)
for i in range(len(alp_L)):
  for j in range(len(L)):
    if alp_L[i] == L[j]:
      total_L[i] = j
      break
print(' '.join(map(str,total_L)))