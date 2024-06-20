#
from input1 import _INPUT
import io, sys
sys.stdin = io.StringIO(_INPUT)

from collections import Counter
day = Counter()
N = int(input())
A = [None] * N
B = [None] * N
max = 0
# データ取得
for i in range(N):
    A[i], B[i] = map(int, input().split())
    if max < B[i]:
        max = B[i]
# 出勤開始日に１人増え、退勤日翌日に１人減る
for i in range(N):
    day[A[i]] += 1
    day[B[i] + 1] -= 1
# 累積和
for i in range(1, max + 1):
    day[i] = day[i - 1] + day[i]
# 連勤数をカウント
count = 0
max_count = 0
for i in range(1, max + 1):
    if day[i] > 0:
        count += 1
    if day[i] == 0 or i == max:
        if max_count < count:
            max_count = count
        count = 0

print(max_count)