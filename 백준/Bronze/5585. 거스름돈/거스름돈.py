import sys
exc = 1000 - int(input())
total = 0
while exc != 0:
  if exc >= 500:
    exc -= 500
    total += 1
  elif exc >= 100:
    tem, t = exc // 100, exc % 100
    total += tem
    exc = t
  elif exc >= 50:
    tem, t = exc // 50, exc % 50
    total += tem
    exc = t
  elif exc >= 10:
    tem, t = exc // 10, exc % 10
    total += tem
    exc = t
  elif exc >= 5:
    tem, t = exc // 5, exc % 5
    total += tem
    exc = t
  elif exc >= 1:
    total += exc
    exc -= exc
print(total)