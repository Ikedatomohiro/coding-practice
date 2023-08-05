# https://paiza.jp/works/mondai/a_rank_level_up_problems/a_rank_calculation_step2
from input2 import _INPUT
import io, sys
sys.stdin = io.StringIO(_INPUT)

N = int(input())
M = 1000003
P = 2
ans = 1
# while N > 0:
#     if N & 1 == 1:
#         ans = ans * P % M
#     P = P * P % M
#     N >>= 1

ans = pow(2, N, M)
print(ans)
