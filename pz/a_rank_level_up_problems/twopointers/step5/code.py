# https://paiza.jp/works/mondai/a_rank_level_up_problems/a_rank_twopointers_step5
from input1 import _INPUT
import io, sys
sys.stdin = io.StringIO(_INPUT)

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
A = [0] * (N + 1)

for i in range(M):
    l, u, a = map(int, input().split())
    A[l - 1] += a
    A[u] -= a

for i in range(N):
    print(numbers[i] + A[i])
    A[i + 1] += A[i]


