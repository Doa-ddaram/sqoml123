a = list(input())
t = 10
for i in range(0,len(a)-1):
  if a[i] == a[i+1]:
    t += 5
  else:
    t += 10
print(t)