# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_d
from input3 import _INPUT
import io, sys
sys.stdin = io.StringIO(_INPUT)

N = int(input())
ans = ""
while N >= 1:
    ans = str(N%2) + ans
    N = int(N / 2)
print("{:010}".format(int(ans)))
