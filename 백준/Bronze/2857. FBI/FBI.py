L = []
for i in range(5):
    S = input()
    for j in range(len(S)-2):
        if S[j] == 'F':
            if S[j+1] == 'B':
                if S[j+2] == 'I':
                    L.append(i+1)
                    break
if len(L) == 0:
    print('HE GOT AWAY!')
else:
    for i in L:
        print(i, end = ' ')