#
from input2 import _INPUT
import io, sys
sys.stdin = io.StringIO(_INPUT)

N = int(input())
S_1 = input()
S_2 = input()

for i in range(N):
    if S_1 == S_2[i:] + S_2[:i]:
        print("Yes")
        exit()
print("No")
