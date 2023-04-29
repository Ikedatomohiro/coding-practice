#
from input2 import _INPUT
import io, sys
sys.stdin = io.StringIO(_INPUT)

N, M = map(int, input().split())
s = [0 for _ in range(N + 1)]
t = [0 for _ in range(N + 1)]

for i in range(M):
    a = int(input())
    s[a] += 1
for i in range(M):
    b = int(input())
    t[b] += 1

ans = "Yes"
for i in range(1, N + 1):
    if s[i] != t[i]:
        ans = "No"
        break
print(ans)
