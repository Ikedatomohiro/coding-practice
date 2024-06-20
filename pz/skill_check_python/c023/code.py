#
from input2 import _INPUT
import io, sys
sys.stdin = io.StringIO(_INPUT)

a = set(list(map(int, input().split())))
N = int(input())
for i in range(N):
    ans = 0
    b = set(list(map(int, input().split())))
    diff = b - a
    print(len(a) - len(diff))
