#
from input2 import _INPUT
import io, sys
sys.stdin = io.StringIO(_INPUT)

N = int(input())
list = list(map(int, input().split()))
list.sort()
list.append(102)
score = 0
for i in range(N):
    if list[i + 1] > list[i] + 1:
        score += list[i]
print(score)