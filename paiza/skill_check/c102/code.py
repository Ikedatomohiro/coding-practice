#
from input1 import _INPUT
import io, sys
sys.stdin = io.StringIO(_INPUT)

M = int(input())
a = []
for _ in range(M):
    a.append(int(input()))
N = int(input())
b = []
for _ in range(N):
    b.append(int(input()))
kaburi = "A"
for i in range(1, 32):
    if i in a and i in b:
        print(kaburi)
        if kaburi == "A":
            kaburi = "B"
        else:
            kaburi = "A"
    elif i in a:
        print("A")
    elif i in b:
        print("B")
    else:
        print("x")
