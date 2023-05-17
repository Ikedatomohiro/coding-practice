# https://paiza.jp/works/mondai/a_rank_level_up_problems/a_rank_twopointers_boss
from input3 import _INPUT
import io, sys
sys.stdin = io.StringIO(_INPUT)

N, K = map(int, input().split())
numbers = list(map(int, input().split()))
A = [1] * (N + 1)
for i in range(N):
    if numbers[i] == 0:
        A[i + 1] = 0
        continue
    if A[i] == 0:
        A[i + 1] = numbers[i]
    else:
        A[i + 1] = A[i] * numbers[i]
A = A[1:]

length = float("inf")
start = 0
end = 0

while True:
    if end >= N or start > end:
        break
    if A[end] >= K:
        if end - start + 1 < length:
            length = end - start + 1
        if A[end] // A[start] < K:
            end += 1
        else:
            start += 1
    elif numbers[end] == 0:
        start = end + 1
        end += 1
    else:
        end += 1

print(length)