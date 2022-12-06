import sys                                                       #2621번 미완성본
color_L = []
number_L = []
for i in range(5):
  a, b= map(str,input().split())
  color_L.append(a)
  number_L.append(int(b))
number_L.sort(reverse=1)
color_L.sort()
if color_L[0] == color_L[4] and (number_L == list(range(number_L[0],number_L[4]-1,-1))):
  print(900+number_L[0])
elif number_L[0] == number_L[3] or number_L[1] == number_L[4]:
  if number_L[0] == number_L[3]:
    print(800 + number_L[0])
  else:
    print(800 + number_L[1])
elif number_L[0] == number_L[2] and number_L[3] == number_L[4]:
  print(700 + (10 * number_L[0]) + number_L[3])
elif number_L[0] == number_L[1] and number_L[2] == number_L[4] :
  print(700 + (10 * number_L[2]) + number_L[0])
elif color_L[0] == color_L[4]:
  print(600 + number_L[0])
elif number_L == list(range(number_L[0],number_L[4]-1,-1)):
  print(500 + number_L[0])
elif number_L[0] == number_L[2]:
  print(400 + number_L[0])
elif number_L[1] == number_L[3]:
  print(400 + number_L[1])
elif number_L[2] == number_L[4]:
  print(400 + number_L[2])
elif number_L[0] == number_L[1] and number_L[2] == number_L[3]:
  print(300 + (10 * number_L[0]) + number_L[2])
elif number_L[0] == number_L[1] and number_L[3] == number_L[4]:
  print(300 + (10 * number_L[0]) + number_L[3])
elif number_L[1] == number_L[2] and number_L[3] == number_L[4]:
  print(300 + (10 * number_L[1]) + number_L[3])
elif number_L[0] == number_L[1]:
  print(200 + number_L[0])
elif number_L[1] == number_L[2]:
  print(200 + number_L[1])
elif number_L[2] == number_L[3]:
  print(200 + number_L[2])
elif number_L[3] == number_L[4]:
  print(200 + number_L[3])
else:
  print(100 + number_L[0])