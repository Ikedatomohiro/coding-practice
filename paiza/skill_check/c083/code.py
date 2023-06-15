#
from input2 import _INPUT
import io, sys
sys.stdin = io.StringIO(_INPUT)

N, R = map(int, input().split())
max = 0
list = {}
for i in range(1, N + 1):
    a = int(input())
    if a > max:
        max = a
    list[i] = a

for i in range(1, N + 1):
    print(f"{i}:{'*' * (list[i] // R)}{'.' * (max // R - list[i] // R)}")
