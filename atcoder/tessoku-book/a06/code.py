#
from input1 import _INPUT
import io, sys
sys.stdin = io.StringIO(_INPUT)
# 全ケースごとに計算しているのが無駄
# N, Q = map(int, input().split())
# guest = list(map(int, input().split()))
# for i in range(Q):
#     L, R = map(int, input().split())
#     count = 0
#     for j in range(L - 1, R):
#         count += guest[j]
#     print(count)


N, Q = map(int, input().split())
guest = list(map(int, input().split()))
total = [0] * (N + 1)
for i in range(len(guest)):
    total[i + 1] = total[i] + guest[i]

for i in range(Q):
    L, R = map(int, input().split())
    ans = total[R] - total[L - 1]
    print(ans)
