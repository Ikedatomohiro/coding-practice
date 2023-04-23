# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_h
from input1 import _INPUT
import io, sys
sys.stdin = io.StringIO(_INPUT)

H, W = map(int, input().split())
s = [list(map(int, input().split())) for _ in range(W)]
t = [[0 for _ in range(H + 1)] for _ in range(W + 1)]

for i in range(1, H + 1):
    for j in range(1, W + 1):
        t[i][j] = t[i][j - 1] + s[i - 1][j - 1]
for j in range(1, W + 1):
    for i in range(1, H + 1):
        t[i][j] = t[i - 1][j] + t[i][j]
Q = int(input())
for i in range(Q):
    A, B, C, D = map(int, input().split())
    ans = t[C][D] - t[A - 1][D] - t[C][B - 1] + t[A - 1][B - 1]
    print(ans)

