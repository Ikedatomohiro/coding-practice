# https://paiza.jp/works/mondai/a_rank_level_up_problems/a_rank_twopointers_step4
from input2 import _INPUT
import io, sys
sys.stdin = io.StringIO(_INPUT)

N, M = map(int, input().split())
numbers = list(map(int, input().split()))

sums = [0]
for i in range(N):
    sums.append(sums[i] + numbers[i])

count  = int(0)
start = 0
end = 0
while True:
    if end >= N:
        break
    if sums[end + 1] - sums[start] <= M:
        count = max(count, end - start + 1)
        end += 1
    else:
        start += 1

print(count)
