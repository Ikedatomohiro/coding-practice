#
from input1 import _INPUT
import io, sys
sys.stdin = io.StringIO(_INPUT)

H, W, X = map(int, input().split())
string = ""
for _ in range(H):
    string += input()
for index, i in enumerate(string):
    print(i, end="")
    if (index + 1) % X == 0 or index == len(string) - 1:
        print()
