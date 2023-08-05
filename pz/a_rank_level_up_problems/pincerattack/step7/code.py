# https://paiza.jp/works/mondai/a_rank_level_up_problems/a_rank_pincerattack_step7
from input2 import _INPUT
import io, sys
sys.stdin = io.StringIO(_INPUT)

H, W, N = map(int, input().split())
s = [list(input()) for i in range(H)]

def reverse(s, sy, sx, dy, dx):
    for i in range(4):
        reverse = []
        y = sy
        x = sx
        while True:
            y += dy[i]
            x += dx[i]
            if y < 0 or y >= H or x < 0 or x >= W or s[y][x] == "#":
                break
            if s[y][x] == ".":
                reverse.append((y, x))
            # マスが＊の場合、reverseのマスを＊に変える
            if s[y][x] == "*":
                for y, x in reverse:
                    s[y][x] = "*"
                break

for i in range(N):
    sy, sx = map(int, input().split())
    s[sy][sx] = "*"
    # 縦横
    dy = (-1, 0, 1, 0)
    dx = (0, 1, 0, -1)
    reverse(s, sy, sx, dy, dx)

    # 斜め
    dy = (-1, -1, 1, 1)
    dx = (-1, 1, -1, 1)
    reverse(s, sy, sx, dy, dx)

for row in s:
    print("".join(row))