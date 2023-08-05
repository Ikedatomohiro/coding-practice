# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_e
from input2 import _INPUT
import io, sys
sys.stdin = io.StringIO(_INPUT)

N, K = map(int, input().split())
ans = 0
for i in range(1, N + 1):
    for j in range(1, N + 1):
        k = K - i - j
        if k >= 1 and k <= N:
            ans += 1
print(ans)