#
from input2 import _INPUT
import io, sys
sys.stdin = io.StringIO(_INPUT)

N = int(input())
graph = [[0] * N for _ in range(N)]

for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a - 1][b - 1] = 1
    graph[b - 1][a - 1] = 1
count = {}
for i in range(N):
    A = int(input())
    count[i] = A
total = 0
index = 0
next_index = 0
for _ in range(N):
    total += count[index]
    print(total)
    if 1 in graph[index]:
        next_index = graph[index].index(1)
        graph[next_index][index] = 0
        index = next_index
