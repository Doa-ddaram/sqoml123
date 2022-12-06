import sys
lines = sys.stdin.readlines()
p=1
count=1
for line in lines:
    n=int(line)
    while True:
      if(p % n==0):
        print(count)
        p = 1
        count = 1
        break
      p = p * 10 + 1
      count += 1