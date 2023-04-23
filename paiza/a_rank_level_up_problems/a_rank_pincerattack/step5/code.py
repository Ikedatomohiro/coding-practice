# https://paiza.jp/works/mondai/a_rank_level_up_problems/a_rank_pincerattack_step5
from input2 import _INPUT
import io, sys
sys.stdin = io.StringIO(_INPUT)

H, W, Y, X = map(int, input().split())
s = [list(input()) for _ in range(H)]
s[Y][X] = "*"
def reverse(s, Y, X, dy, dx):
    for i in range(4):
        ny = Y
        nx = X
        reverse = []
        while True:
            ny += dy[i]
            nx += dx[i]
            if ny < 0 or ny >= H or nx < 0 or nx >= W:
                break
            if s[ny][nx] == ".":
                reverse.append((ny, nx))
            if s[ny][nx] == "*":
                for y, x in reverse:
                    s[y][x] = "*"
                break

# 縦横
dy = (-1, 0, 1, 0)
dx = (0, 1, 0, -1)
reverse(s, Y, X, dy, dx)
# 斜め
dy = (-1, -1, 1, 1)
dx = (-1, 1, 1, -1)
reverse(s, Y, X, dy, dx)

for row in s:
    print("".join(row))
