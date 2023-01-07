n = int(input())
from collections import deque
card_q = deque(range(1,n+1))
t = 0
while True:
  t += 1
  if len(card_q) == 1:
    break
  card_q.popleft()
  if len(card_q) == 1:
    break
  card_q.append(card_q.popleft())
print(card_q[0])