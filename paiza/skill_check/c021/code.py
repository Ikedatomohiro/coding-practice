#
from input2 import _INPUT
import io, sys
sys.stdin = io.StringIO(_INPUT)

xc, yc, r_1, r_2 = map(int, input().split())
n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    if r_1 ** 2 <= (x - xc) ** 2 + (y - yc) ** 2 <= r_2 ** 2:
        print("yes")
    else:
        print("no")