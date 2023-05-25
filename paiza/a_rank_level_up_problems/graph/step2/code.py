# https://paiza.jp/works/mondai/a_rank_level_up_problems/a_rank_graph_step2
from input2 import _INPUT
import io, sys
sys.stdin = io.StringIO(_INPUT)

N, M = map(int, input().split())
g = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    g[a - 1].append(b - 1)
    g[b - 1].append(a - 1)

for row in g:
    row.sort()
    for r in row:
        print(r, end="")
    print()
