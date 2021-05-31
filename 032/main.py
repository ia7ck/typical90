#!/usr/bin/env python3

import itertools

n = int(input())
a = [[] for _ in range(n)]
for i in range(n):
    a[i] = list(map(int, input().split()))
m = int(input())
ng = [[False] * n for _ in range(n)]
for _ in range(m):
    x, y = map(int, input().split())
    ng[x - 1][y - 1] = ng[y - 1][x - 1] = True

inf = 1_000_000_000
ans = inf
for p in itertools.permutations(range(n)):
    cost = 0
    for i in range(n):
        cost += a[p[i]][i]
    if cost >= ans:
        continue
    ok = True
    for i in range(n - 1):
        x = p[i]
        y = p[i + 1]
        if ng[x][y]:
            ok = False
            break
    if ok:
        ans = cost
if ans == inf:
    print(-1)
else:
    print(ans)
