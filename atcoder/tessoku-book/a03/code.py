# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_c
from input2 import _INPUT
import io, sys
sys.stdin = io.StringIO(_INPUT)

N, K = map(int, input().split())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))

ans = "No"
for i in range(N):
    if K - P[i] in Q:
        ans = "Yes"
print(ans)
