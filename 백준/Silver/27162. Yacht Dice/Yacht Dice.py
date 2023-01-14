import sys
input = sys.stdin.readline
y_L = list(map(str,input().rstrip()))
x_L = list(map(int,input().split()))
x_L.sort()
count = 0
if x_L[0] == x_L[1] and x_L[1] == x_L[2]:
    count = 2
elif x_L[0] == x_L[1] or x_L[1] == x_L[2]:
    count = 1
t_L = [0 for i in range(12)]
for i in range(3):
    if y_L[x_L[i]-1] == 'Y':
        t_L[x_L[i]-1] = t_L[x_L[i]-1] + x_L[i]
for i in range(6):
    if y_L[i] == 'Y':
        t_L[i] = t_L[i] + 2 * (i + 1)
if y_L[6] == 'Y':
    if count >= 1:
        t_L[6] = x_L[1] * 4
if y_L[7] == 'Y':
    if count == 2:
        if x_L[1] != 6:
            t_L[7] = x_L[1] * 3 + 6 * 2
        else:
            t_L[7] = x_L[1] * 3 + 5 * 2
    elif count == 1:
        if x_L[0] == x_L[1]:
            t_L[7] = x_L[1] * 2 + x_L[2] * 3
        else:
            t_L[7] = x_L[0] * 2 + x_L[1] * 3
if y_L[8] == 'Y':
    temp = 0
    for so in x_L:
        if so == 6:
            temp = 1
    if temp == 0 and count == 0:
        t_L[8] = 30
if y_L[9] == 'Y':
    temp = 0
    for so in x_L:
        if so == 1:
            temp = 1
    if temp == 0 and count == 0:
        t_L[9] = 30
if y_L[10] == 'Y':
    if count == 2:
        t_L[10] = 50
if y_L[11] == 'Y':
    t_L[11] = sum(x_L) + 12
Max = max(t_L)
print(Max)