#
from input2 import _INPUT
import io, sys
sys.stdin = io.StringIO(_INPUT)

a, b, R = map(int, input().split())
N = int(input())
for _ in range(N):
    x, y = map(int, input().split())
    if (x - a) ** 2 + (y - b) ** 2 >= R ** 2:
        print("silent")
    else:
        print("noisy")
