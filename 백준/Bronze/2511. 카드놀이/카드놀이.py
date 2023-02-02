a_L = list(map(int,input().split()))
b_L = list(map(int,input().split()))
a,b = 0,0
temp = 'D'
for i in range(10):
    if a_L[i] > b_L[i]:
        a += 3
        temp = 'A'
    elif b_L[i] > a_L[i]:
        b += 3
        temp = 'B'
    else:
        a += 1
        b += 1
print(a,b)
if a > b:
    print('A')
elif a < b:
    print('B')
else:
    print(temp)