a, b = map(int, input().split())
if a == 0 :
    a += 24
c = a * 60 + b - 45
a = c // 60
if a == 24 :
    a -= 24
b = c % 60
print(a, b)