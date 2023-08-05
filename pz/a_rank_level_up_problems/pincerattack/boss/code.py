# https://paiza.jp/works/mondai/a_rank_level_up_problems/a_rank_pincerattack_boss
from input2 import _INPUT
import io, sys
sys.stdin = io.StringIO(_INPUT)

H, W, N, n = map(int, input().split())
s = [list(input()) for _ in range(H)]

def reverse(s, sy, sx, dy, dx, p):
    tmpS = s
    s[sy][sx] = str(p)
    for i in range(4):
        reverse = []
        y = sy
        x = sx
        while True:
            y += dy[i]
            x += dx[i]
            if y < 0 or y >= H or x < 0 or x >= W or tmpS[y][x] == "#":
                break
            reverse.append([y, x])
            if tmpS[y][x] == str(p):
                for y, x in reverse:
                    s[y][x] = str(p)
                break

dyvl = [0, 1, 0, -1]
dxvl = [1, 0, -1, 0]
dysl = [1, 1, -1, -1]
dxsl = [1, -1, -1, 1]

for _ in range(n):
    p, sy, sx = map(int, input().split())
    reverse(s, sy, sx, dyvl, dxvl, p)
    reverse(s, sy, sx, dysl, dxsl, p)

for row in s:
    print("".join(row))
