a =int(input())
b = int(input())
c = b
for i in range(0,3):
    print('%d' %(a * (c%10)))
    c = c // 10
print(a * b)