a = int(input())
i = 2
while a != 1:
  if a % i == 0:
    print(i)
    a /= i
    i = 1
  i += 1