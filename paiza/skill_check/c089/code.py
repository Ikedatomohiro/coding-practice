#
from input2 import _INPUT
import io, sys
sys.stdin = io.StringIO(_INPUT)

H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]
P = [list(input().split()) for _ in range(H)]
score = 0
for i in range(H):
    for j in range(W):
        if S[i][j] == "o":
            score += int(P[i][j])

print(score)