import sys
for _ in range(int(input())):
  p = int(input())
  soccer_dic = dict()
  for i in range(p):
    price, name = map(str,input().split())
    price = int(price)
    soccer_dic[name] = price
  soccer_dic = sorted(soccer_dic.items(), key = lambda x : x[1], reverse = True)
  print(soccer_dic[0][0])