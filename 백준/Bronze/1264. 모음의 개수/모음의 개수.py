vow_L = ['a','e','i','o','u','A','E','I','O','U']
while True:
    t = input()
    if t == '#':
        break
    total = 0
    for i in range(len(t)):
        if t[i] in vow_L:
            total += 1
    print(total)