import sys                                        #2577번 
num = 1
for _ in range(3):
  num *= int(input())
num = str(num)
for i in range(10):
  print(num.count(str(i)))