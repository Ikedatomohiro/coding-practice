# https://paiza.jp/works/mondai/a_rank_level_up_problems/a_rank_pincerattack_step8
from input3 import _INPUT
import io, sys
sys.stdin = io.StringIO(_INPUT)

H, W, N = map(int, input().split())
s = [list(input()) for i in range(H)]
def reverse(s, sy, sx, dy, dx, P):
    tmpS = s.copy()
    s[sy][sx] = P
    for i in range(4):
        reverse = []
        y = sy
        x = sx
        nonP = "A"
        if P == "A":
            nonP = "B"
        while True:
            y += dy[i]
            x += dx[i]
            if y < 0 or y >= H or x < 0 or x >= W or tmpS[y][x] == "#":
                break
            if tmpS[y][x] == "." or tmpS[y][x] == nonP:
                reverse.append((y, x))
            # マスがPの場合、reverseのマスをPに変える
            if tmpS[y][x] == P:
                for y, x in reverse:
                    s[y][x] = P
                break

dyvl = (-1, 0, 1, 0)
dxvl = (0, 1, 0, -1)
dysl = (-1, -1, 1, 1)
dxsl = (-1, 1, -1, 1)

for i in range(N):
    # 先行Aさん
    sy, sx = map(int, input().split())
    reverse(s, sy, sx, dyvl, dxvl, "A")
    reverse(s, sy, sx, dysl, dxsl, "A")
    # 後攻Bさん
    sy, sx = map(int, input().split())
    reverse(s, sy, sx, dyvl, dxvl, "B")
    reverse(s, sy, sx, dysl, dxsl, "B")

for row in s:
    print("".join(row))
