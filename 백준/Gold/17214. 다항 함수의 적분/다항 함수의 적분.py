import sys                    #17214
orif = input()
input = sys.stdin.readline
t = 0
for i in range(len(orif)):
  if orif[i] == 'x':
    t += 1
    if i+1 < len(orif) and orif[i+1] == '-':
      t += 2
  elif orif[i] == '+':
    t += 1
if t == 3:
  temp = list(map(int,orif.split('x-')))
  if temp[0] == 2:
    if temp[1] == 1:
      print('xx-x+W')
    else:
      print('xx-%dx+W' %(temp[1]))
  elif temp[0] == -2:
    if temp[1] == 1:
      print('-xx-x+W')
    else:
      print('-xx-%dx+W' %(temp[1]))
  else:
    if temp[1] == 1:
      print('%dxx-x+W'%(temp[0] // 2))
    else:
      print('%dxx-%dx+W' %(temp[0]//2, temp[1]))
elif t == 2:
  temp = list(map(int,orif.split('x+')))
  if temp[0] == 2:
    if temp[1] == 1:
      print('xx+x+W')
    else:
      print('xx+%dx+W' %(temp[1]))
  elif temp[0] == -2:
    if temp[1] == 1:
      print('-xx+x+W')
    else:
      print('-xx+%dx+W' %(temp[1]))
  else:
    if temp[1] == 1:
      print('%dxx+x+W' %(temp[0]//2))
    else:
      print('%dxx+%dx+W' %(temp[0]//2, temp[1]))
elif t == 1:
  temp = orif[:-1]
  if temp == '2':
    print('xx+W')
  elif temp == '-2':
    print('-xx+W')
  else:
    print('%dxx+W'%(int(temp) // 2))
else:
  if orif == '0':
    print('W')
  elif orif == '-1':
    print('-x+W')
  elif orif == '1':
    print('x+W')
  else:
    print('%dx+W'%(int(orif)))