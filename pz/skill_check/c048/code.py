#
from input2 import _INPUT
import io, sys
sys.stdin = io.StringIO(_INPUT)

X, P = map(int, input().split())
price = X
total = X
while price > 0:
    price = int(price * (100 - P) / 100)
    total += price

print(total)