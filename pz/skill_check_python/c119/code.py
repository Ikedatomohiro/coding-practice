#
from input2 import _INPUT
import io, sys
sys.stdin = io.StringIO(_INPUT)

N, M, K = map(int, input().split())

m = [0 for i in range(M)]
for i in range(M):
    m[i] = int(input())

ans = 0
ret = 0
for i in range(1, N + 1):
    if i not in m:
        ans += 1
        ret = 0
    else:
        ret += 1
        if ret == K:
            break
print(ans)