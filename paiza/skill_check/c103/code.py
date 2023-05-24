#
from input1 import _INPUT
import io, sys
sys.stdin = io.StringIO(_INPUT)

N, M = map(int, input().split())
l = []
for _ in range(M):
    A, B = input().split()
    l.append((int(A), B))
for i in range(1, N + 1):
    L = []
    for t in l:
        if i % t[0] == 0:
            L.append(t[1])
    if L == []:
        print(i)
    else:
        print(" ".join(L))
