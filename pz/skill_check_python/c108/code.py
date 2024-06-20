#
from input2 import _INPUT
import io, sys
sys.stdin = io.StringIO(_INPUT)

N = int(input())
x = [int(input()) for _ in range(N)]
c = [list(map(int, input().split())) for _ in range(N)]
K = int(input())

time = 0
f = 0
for i in range(K):
    y = int(input())
    if i == 0:
        f = y
    time = time + x[y - 1] + c[f - 1][y - 1]
    f = y

print(time)
