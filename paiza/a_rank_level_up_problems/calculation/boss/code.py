# https://paiza.jp/works/mondai/a_rank_level_up_problems/a_rank_calculation_boss
from input2 import _INPUT
import io, sys
sys.stdin = io.StringIO(_INPUT)

A, B = map(int, input().split())

while B > 0:
    R = A % B
    A = B
    B = R
    print(A, B)

print(A)