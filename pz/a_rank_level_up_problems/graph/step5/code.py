# https://paiza.jp/works/mondai/a_rank_level_up_problems/a_rank_graph_step5
from input1 import _INPUT
import io, sys
sys.stdin = io.StringIO(_INPUT)

N = int(input())

graph = [[0] * N for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a - 1][b - 1] = 1
    graph[b - 1][a - 1] = 1

index = 0
next_index = 0
for _ in range(N):
    print(index + 1)
    if 1 in graph[index]:
        next_index = graph[index].index(1)
        graph[next_index][index] = 0
        index = next_index
