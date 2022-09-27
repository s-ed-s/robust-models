import collections


c = collections.Counter(map(int, input().split(" ")))
k = int(input())
items = sorted(c.items(), key=lambda p: p[1], reverse=True)

print([el[0] for el in items[:k]])