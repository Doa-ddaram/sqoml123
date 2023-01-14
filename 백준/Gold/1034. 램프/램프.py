import sys
input = sys.stdin.readline
n, m = map(int, input().split())
L = [input().rstrip() for i in range(n)]
    
k = int(input())

Max = 0

for i in range(n):
    temp = 0
    for j in L[i]:
        if j == '0':
            temp += 1
        
    total = 0
    if temp <= k and temp %2 == k%2:  
        for r in range(n):  
            if L[i] == L[r]:  
                total += 1
                
    Max = max(Max, total)
    
print(Max)