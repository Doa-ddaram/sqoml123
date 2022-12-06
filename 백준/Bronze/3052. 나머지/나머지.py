import sys

S = set()
for _ in range(10):
  i = int(input())
  S.add(i % 42)
print(len(S))