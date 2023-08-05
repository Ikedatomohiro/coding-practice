# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_i
from input1 import _INPUT
import io, sys
sys.stdin = io.StringIO(_INPUT)

# 以下のコードは累積和を活用できていない。前半部分はそのまま全エリアの計算して行っているので時間がかかっている。
# H, W, N = map(int, input().split())
# sum = [[0] * (W + 1) for _ in range(H + 1)]
# for _ in range(N):
#     A, B, C, D = map(int, input().split())
#     A -= 1
#     B -= 1
#     for i in range(A, C):
#         sum[i][B] += 1
#         sum[i][D] -= 1

# for i in range(H):
#     for j in range(1, W):
#         if j - 1 >= 0:
#             sum[i][j] += sum[i][j - 1]

# for row in sum[:-1]:
#     print(" ".join(map(str, row[:-1])))

H, W, N = map(int, input().split())
ans = [[0] * (W + 1) for _ in range(H + 1)]
for _ in range(N):
    x1, y1, x2, y2 = map(int, input().split())
    x1 -= 1
    y1 -= 1

    ans[x1][y1] += 1
    ans[x1][y2] -= 1
    ans[x2][y1] -= 1
    ans[x2][y2] += 1

for i in range(H):
    for j in range(W):
        if i - 1 >= 0:
            ans[i][j] += ans[i - 1][j]

for i in range(H):
    for j in range(W):
        if j - 1 >= 0:
            ans[i][j] += ans[i][j - 1]

for row in ans[:-1]:
    print(*row[:-1])
