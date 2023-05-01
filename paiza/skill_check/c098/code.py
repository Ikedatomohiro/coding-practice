#
from input2 import _INPUT
import io, sys
sys.stdin = io.StringIO(_INPUT)

N = int(input())
s = [ None ] * (N + 1)
for i in range(1, N + 1):
    s[i] = int(input())
M = int(input())

for i in range(M):
    a, b, x = map(int, input().split())
    if s[a] < x:
        s[b] += s[a]
        s[a] = 0
    else:
        s[b] += x
        s[a] -= x

for i in range(1, N + 1):
    print(s[i])