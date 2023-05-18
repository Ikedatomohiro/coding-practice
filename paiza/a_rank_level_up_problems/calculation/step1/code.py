# https://paiza.jp/works/mondai/a_rank_level_up_problems/a_rank_calculation_exchange_700
from input1 import _INPUT
import io, sys
sys.stdin = io.StringIO(_INPUT)

N, K = map(int, input().split())

def calc(n):
    if n % 3 == 0:
        return 0
    elif n % 3 == 1 or n % 3 == 2:
        return 1

ans = 0
if (N == K):
    ans = calc(N)
else:
    N -= 1
n_total = calc(N)
k_total = calc(K)
ans = k_total - n_total

print(ans)