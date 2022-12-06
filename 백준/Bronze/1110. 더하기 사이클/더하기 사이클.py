n = int(input())
t = 1000
k = 0
a = n // 10
b = n % 10
while t != n:
    k += 1
    t = b * 10 + ((a + b) % 10)
    a = t // 10
    b = t % 10
print(k)