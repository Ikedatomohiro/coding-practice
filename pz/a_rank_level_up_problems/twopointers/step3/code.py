# https://paiza.jp/works/mondai/a_rank_level_up_problems/a_rank_twopointers_step3
from input3 import _INPUT
import io, sys
sys.stdin = io.StringIO(_INPUT)

N, M = map(int, input().split())
numbers = list(map(int, input().split()))

sums = [0]
for i in range(N):
    sums.append(sums[i] + numbers[i])
count  = float("inf")
start = 0
end = 0
while True:
    if end >= N:
        break
    if sums[end + 1] - sums[start] >= M:
        count = min(count, end - start + 1)
        start += 1
    else:
        end += 1

if count == float("inf"):
    count = -1
print(count)


exit()
N, M = map(int, input().split())
A = list(map(int, input().split()))
length = 0
ans = -1
sum = 0
start = 0
end = 0
for i in range(N):
    sum += A[i]
    if sum < M:
        end = i
    elif sum >= M:
        while sum >= M:
            sum -= A[start]
            start += 1
            length = end - start + 1
    if ans > length or ans <= 0:
        ans = length
if ans <= 0:
    ans = -1
print(ans)
