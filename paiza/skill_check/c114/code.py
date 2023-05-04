#
from input3 import _INPUT
import io, sys
sys.stdin = io.StringIO(_INPUT)

N = int(input())
A = [input() for _ in range(N)]
for i in range(N - 1):
    if A[i][-1] != A[i + 1][0]:
        print(A[i][-1], A[i + 1][0])
        exit()
print("Yes")



