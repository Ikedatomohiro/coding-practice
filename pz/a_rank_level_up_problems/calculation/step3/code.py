# https://paiza.jp/works/mondai/a_rank_level_up_problems/a_rank_calculation_step3
from input2 import _INPUT
import io, sys
sys.stdin = io.StringIO(_INPUT)

import math
N = int(input())
ans = "NO"
if N == 2:
    ans = "YES"
if N > 2 and N % 2 != 0:
    for i in range(3, int(math.sqrt(N)) + 1, 2):
        if N % i == 0:
            ans = "NO"
            break
        ans = "YES"
print(ans)