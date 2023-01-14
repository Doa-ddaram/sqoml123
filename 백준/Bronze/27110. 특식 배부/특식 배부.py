n = int(input())
A,B,C = map(int,input().split())
total = 0
if A<n:
    total += A
else:
    total += n
if B<n:
    total += B
else:
    total += n
if C<n:
    total += C
else:
    total += n
print(total)