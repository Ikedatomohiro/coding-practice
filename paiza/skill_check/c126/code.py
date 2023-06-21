#
from input2 import _INPUT
import io, sys
sys.stdin = io.StringIO(_INPUT)

shin, hotel, N = map(int, input().split())
total = 0
before_end = 0
for i in range(N):
    start, end = list(map(int, input().split()))
    if i == 0:
        total += shin
    else:
        hotel_total = hotel * (start - before_end)
        shin_total = shin * 2
        total += min(hotel_total, shin_total)
    before_end = end
total += shin
print(total)