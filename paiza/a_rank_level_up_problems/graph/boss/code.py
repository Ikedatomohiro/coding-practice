# https://paiza.jp/works/mondai/a_rank_level_up_problems/a_rank_graph_boss
from input2 import _INPUT
import io, sys
sys.stdin = io.StringIO(_INPUT)

N, M = map(int, input().split())
graph = [[0] * N for _ in range(N)]
visited = [False] * N

from collections import deque
d = deque()

for _ in range(M):
    a, b = map(int, input().split())
    graph[a - 1][b - 1] = 1
    graph[b - 1][a - 1] = 1

index = 1
next_index = 0
visited[index] = True
for index, p in enumerate(graph[index]):
    if p == 1:
        d.append(index)

while len(d) > 0:
    index = d.popleft()
    visited[index] = True
    for index, p in enumerate(graph[index]):
        if p == 1 and visited[index] == False:
            d.append(index)

if False in visited:
    print("NO")
else:
    print("YES")
