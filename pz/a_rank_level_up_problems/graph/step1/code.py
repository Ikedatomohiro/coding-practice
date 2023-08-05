#
from input2 import _INPUT
import io, sys
sys.stdin = io.StringIO(_INPUT)

N, M = map(int, input().split())
g = [["0" for _ in range(N)] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    g[a - 1][b - 1] = "1"
    g[b - 1][a - 1] = "1"
for row in g:
    print("".join(row))