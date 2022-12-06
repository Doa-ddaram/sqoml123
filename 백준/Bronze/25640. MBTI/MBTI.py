import sys
x = sys.stdin.readline().rstrip()
t = 0
for _ in range(int(sys.stdin.readline())):
    trap = 0
    mbti = sys.stdin.readline().rstrip()
    for i in range(4):
        if x[i] != mbti[i]:
            trap += 1
            break
    if trap == 0:
        t += 1
print(t)