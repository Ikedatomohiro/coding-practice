#
from input3 import _INPUT
import io, sys
sys.stdin = io.StringIO(_INPUT)

N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
X = int(input())
now = 0
ans = 0
cost = 0
for _ in range(X):
    R, S = map(lambda x: int(x) - 1, input().split())
    if now > S:
        cost = A[R][now] - A[R][S]
    elif now < S:
        cost = A[R][S] - A[R][now]
    elif now == S:
        cost = 0
    now = S
    ans += cost
print(ans)
