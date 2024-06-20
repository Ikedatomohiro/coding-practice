#
from input3 import _INPUT
import io, sys
sys.stdin = io.StringIO(_INPUT)

N = int(input())
x = [int(input()) for i in range(N)]
n, d = x[N - 1], 1

for i in range(N - 2, -1, -1):
    n, d = d, n
    n = n + d * x[i]

print(n, d)