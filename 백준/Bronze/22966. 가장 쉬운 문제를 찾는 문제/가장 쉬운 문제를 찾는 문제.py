easy_quest_dic = dict()
for _ in range(int(input())):
  a,b = map(str, input().split())
  easy_quest_dic[a] = b
  easy_quest_sort_dic = sorted(easy_quest_dic.items(), key= lambda x : x[1])
print(easy_quest_sort_dic[0][0])