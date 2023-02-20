n = int(input())
for i in range(n):
    S = input()
    if int(S[-1]) % 2:
        print('odd')
    else:
        print('even')