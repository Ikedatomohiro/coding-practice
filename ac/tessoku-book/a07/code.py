# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_g
from input1 import _INPUT
import io, sys
sys.stdin = io.StringIO(_INPUT)
# タイムアウト
# from collections import Counter
# D = int(input())
# N = int(input())
# count = Counter()
# for _ in range(N):
#     L, R = map(int, input().split())
#     for i in range(L, R + 1):
#         count[i] += 1
# for i in range(1, D + 1):
#     print(count[i])


from collections import Counter
D = int(input())
N = int(input())
L = [ None ] * N
R = [ None ] * N
for i in range(N):
	L[i], R[i] = map(int, input().split())

# 来場初日に１人増え、来場最終日翌日に１人減る
B = Counter()
for i in range(N):
	B[L[i]] += 1
	B[R[i]+1] -= 1
# 累積和
ans = Counter()
for i in range(1, D+1):
    ans[i] = ans[i-1] + B[i]
    print(ans[i])


