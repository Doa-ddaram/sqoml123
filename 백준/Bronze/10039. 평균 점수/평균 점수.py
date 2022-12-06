all = 0
for i in range(0, 5):
  a = int(input())
  if a < 40:
    a = 40
  all += a
print(int(all / 5))