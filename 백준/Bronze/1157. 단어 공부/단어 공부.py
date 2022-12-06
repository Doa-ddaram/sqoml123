sample_L = [0 for i in range(26)]
str_input = input()
for i in range(len(str_input)):
  temp = ord(str_input[i])
  if 97 <= temp <= 122:
    sample_L[temp-97] += 1
  else:
    sample_L[temp-65] += 1
count_L = sorted(sample_L,reverse=True)
if count_L[0] == count_L[1]:
  print('?')
else:
  for i in range(26):
    if sample_L[i] == count_L[0]:
      str_ord = i
      break
  print(chr(i+65))