import sys
a,b,c,d,e,f = map(int,input().split())
deno = a * e - b * d
x_num = e * c - b * f
y_num = a * f - c * d
print(x_num // deno, y_num // deno)