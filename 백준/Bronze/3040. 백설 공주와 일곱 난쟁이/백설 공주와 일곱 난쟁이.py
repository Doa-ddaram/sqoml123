import sys
dwarf_L = []
for _ in range(9):
  dwarf_L.append(int(sys.stdin.readline()))
temp_total = 0
for i in range(9):
  temp_total += dwarf_L[i]
for i in range(len(dwarf_L)-1):
  for j in range(i + 1,len(dwarf_L)):
    if temp_total - 100 == (dwarf_L[i] + dwarf_L[j]):
      del dwarf_L[i]
      del dwarf_L[j-1]
      break
for i in range(7):
  print(dwarf_L[i])