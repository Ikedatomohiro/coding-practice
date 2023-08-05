# https://paiza.jp/works/mondai/a_rank_level_up_problems/a_rank_twopointers_step2
from input2 import _INPUT
import io, sys
sys.stdin = io.StringIO(_INPUT)

N = int(input())
A = list(map(int, input().split()))
# 累積和
sum = [0] * (N + 1)
for i in range(N):
    sum[i] = sum[i - 1] + A[i]
n = int(input())
for _ in range(n):
    l, u = map(int, input().split())
    print(sum[u] - sum[l - 1])

