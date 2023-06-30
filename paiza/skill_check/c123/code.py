#
from input1 import _INPUT
import io, sys
sys.stdin = io.StringIO(_INPUT)

N = int(input())
Y = [0] * (N + 1)
Z = [0] * (N + 1)
for i in range(1, N + 1):
    Y[i] = int(input())

M = int(input())
for _ in range(M):
    A, B, C = map(int, input().split())
    for i in range(A, B + 1):
        if Y[i] <= Z[i] + C:
            Z[i] = Y[i]
        else:
            Z[i] += C

for i in range(1, N + 1):
    print(Z[i])

