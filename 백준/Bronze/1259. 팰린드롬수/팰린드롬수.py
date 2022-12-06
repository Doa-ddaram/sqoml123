import sys
while True:
    N = str(sys.stdin.readline().rstrip())
    t = 0
    if N == '0':
	    break
    for i in range(len(N)//2):
	    if N[i] != N[-1 * i -1]:
	         t = 1
	         break
    if t == 0:
	    print('yes')
    else:
	    print('no')
	