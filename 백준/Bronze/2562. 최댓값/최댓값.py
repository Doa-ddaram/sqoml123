import sys
nine_L = []                       #9개의 자연수가 들어갈 리스트 생성
for _ in range(9):
  nine_L.append(int(sys.stdin.readline()))     #입력받은 모든 숫자들은 리스트에 추가.
Max = nine_L[0]                   #임시 최댓값은 리스트의 처음으로 설정
for i in range(9):
  if nine_L[i] > Max:
    Max = nine_L[i]
print(Max)
print(nine_L.index(Max) + 1)