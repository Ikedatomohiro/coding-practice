#
from input2 import _INPUT
import io, sys
sys.stdin = io.StringIO(_INPUT)

N = int(input())
count = 0
for _ in range(N):
    t, e, m, s, j, g = input().split()
    total = int(e) + int(m) + int(s) + int(j) + int(g)
    if total >= 350:
        if t == "s":
            if int(m) + int(s) >= 160:
                count += 1
        else:
            if int(j) + int(g) >= 160:
                count += 1
print(count)
