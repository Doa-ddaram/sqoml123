import sys
input = sys.stdin.readline
zero_stack = []
for _ in range(int(input())):
    n = int(input())
    if n:
        zero_stack.append(n)
    else:
        zero_stack.pop()
print(sum(zero_stack))