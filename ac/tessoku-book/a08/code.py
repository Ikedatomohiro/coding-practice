# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_h
from input1 import _INPUT
import io, sys
sys.stdin = io.StringIO(_INPUT)

# H, W = map(int, input().split())
# s = [list(map(int, input().split())) for _ in range(W)]
# t = [[0 for _ in range(H + 1)] for _ in range(W + 1)]

# for i in range(1, H + 1):
#     for j in range(1, W + 1):
#         t[i][j] = t[i][j - 1] + s[i - 1][j - 1]
# for j in range(1, W + 1):
#     for i in range(1, H + 1):
#         t[i][j] = t[i - 1][j] + t[i][j]
# Q = int(input())
# for i in range(Q):
#     A, B, C, D = map(int, input().split())
#     ans = t[C][D] - t[A - 1][D] - t[C][B - 1] + t[A - 1][B - 1]
#     print(ans)


H, W = map(int, input().split())
X = [list(map(int, input(). split())) for _ in range(H)]
accum = [[0] * (W + 1) for _ in range(H + 1)]
for i in range(1, H + 1):
    for j in range(1, W + 1):
        accum[i][j] = accum[i - 1][j] + accum[i][j - 1] - accum[i - 1][j - 1] + X[i - 1][j - 1]

Q = int(input())
for _ in range(Q):
    x1, y1, x2, y2 = map(int, input().split())
    x1 -= 1
    y1 -= 1
    print(accum[x1][y1] + accum[x2][y2] - accum[x1][y2] - accum[x2][y1])
