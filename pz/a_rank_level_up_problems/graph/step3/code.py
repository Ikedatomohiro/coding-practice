# https://paiza.jp/works/mondai/a_rank_level_up_problems/a_rank_graph_step3
from input2 import _INPUT
import io, sys
sys.stdin = io.StringIO(_INPUT)

N, M = map(int, input().split())
g = [[] for _ in range(N)]
m = [["0" for _ in range(N)] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    g[a - 1].append(b - 1)
    m[a - 1][b - 1] = "1"

for row in m:
    print("".join(row))

for row in g:
    row.sort()
    for r in row:
        print(r, end="")
    print()
