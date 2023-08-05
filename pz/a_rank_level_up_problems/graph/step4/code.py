# https://paiza.jp/works/mondai/a_rank_level_up_problems/a_rank_graph_step4
from input2 import _INPUT
import io, sys
sys.stdin = io.StringIO(_INPUT)

N, M = map(int, input().split())
graph = [["0" for _ in range(N)] for _ in range(N)]
list = [[] for _ in range(N)]
for _ in range(M):
    a, b, k = input().split()
    graph[int(a)-1][int(b)-1] = k
    list[int(a)-1].append((int(b) - 1, k))
for row in graph:
    print ("".join(row))

for i in range(N):
    if list[i] != []:
        list[i].sort()
        for val in list[i]:
            print(f"{val[0]}({val[1]})", end="")
    print()
