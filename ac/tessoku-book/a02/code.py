# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_b
from input2 import _INPUT
import io, sys
sys.stdin = io.StringIO(_INPUT)

N, X = map(int, input().split())
l = map(int, input().split())
if X in l:
    print("Yes")
else:
    print("No")