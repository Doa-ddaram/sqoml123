a, b, c = map(int, input().split())
inp = int(input())
all = a * 3600 + b * 60 + c + inp
print(all//3600 % 24, all // 60 % 60 , all % 60)
