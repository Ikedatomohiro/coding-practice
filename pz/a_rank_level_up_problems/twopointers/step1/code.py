# https://paiza.jp/works/mondai/a_rank_level_up_problems/a_rank_twopointers_step1
from input2 import _INPUT
import io, sys
sys.stdin = io.StringIO(_INPUT)

N = int(input())
A = list(map(int, input().split()))
total = 0
for i in range(N):
    total += A[i]
    print(total)
