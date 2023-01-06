import sys
input = sys.stdin.readline
st_1_L= list(input().rstrip())
st_2_L = []

for _ in range(int(input())):
    command = input().rstrip()
    if len(command) == 3:
        st_1_L.append(command[-1])
    else:
        if command == 'L':
            if len(st_1_L) == 0:
                continue
            st_2_L.append(st_1_L.pop())
        elif command == 'B':
            if len(st_1_L) == 0:
                continue
            st_1_L.pop()
        elif command == 'D':
            if len(st_2_L) == 0:
                continue
            st_1_L.append(st_2_L.pop())

t_L = st_1_L + st_2_L[::-1]
print(''.join(map(str,t_L)))