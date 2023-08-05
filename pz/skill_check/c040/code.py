#
from input2 import _INPUT
import io, sys
sys.stdin = io.StringIO(_INPUT)

N = int(input())
lowest = 100.0
highest = 200.0
for _ in range(N):
    c, h = input().split()
    if c == "le":
        if highest > float(h):
            highest = float(h)
    else:
        if lowest < float(h):
            lowest = float(h)
print(lowest, highest)