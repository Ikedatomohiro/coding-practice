# https://paiza.jp/works/mondai/a_rank_level_up_problems/a_rank_pincerattack_step8
from input3 import _INPUT
import io, sys
sys.stdin = io.StringIO(_INPUT)

H, W, N = map(int, input().split())
s = [list(input()) for _ in range(H)]
points = [list(map(int, input().split())) for _ in range(N * 2)]
player = "A"


def check_diagonal(x, y, s, player):
    for lr1 in range(-1, 2, 2):
        for lr2 in range(-1, 2, 2):
            i = 0
            while True:
                i += 1
                if (
                    x + i * lr1 < 0
                    or x + i * lr1 >= W
                    or y + i * lr2 < 0
                    or y + i * lr2 >= H
                ):
                    break
                if s[y + i * lr2][x + i * lr1] == player:
                    for j in range(1 + i):
                        s[y + j * lr2][x + j * lr1] = player
                    break
                if s[y + i * lr2][x + i * lr1] == "#":
                    break


def check_row(x, y, s, player):
    for lr in range(-1, 2, 2):
        i = 0
        while True:
            i += 1
            if x + i * lr < 0 or x + i * lr >= W:
                break
            if s[y][x + i * lr] == player:
                for j in range(1 + i):
                    s[y][x + j * lr] = player
                break
            if s[y][x + i * lr] == "#":
                break


def check_column(x, y, s, player):
    for lr in range(-1, 2, 2):
        i = 0
        while True:
            i += 1
            if y + i * lr < 0 or y + i * lr >= H:
                break
            if s[y + i * lr][x] == player:
                for j in range(1 + i):
                    s[y + j * lr][x] = player
                break
            if s[y + i * lr][x] == "#":
                break
for y, x in points:
    s[y][x] = player
    check_row(x, y, s, player)
    check_column(x, y, s, player)
    check_diagonal(x, y, s, player)
    if player == "A":
        player = "B"
    else:
        player = "A"

for y in range(H):
    for x in range(W):
        print(s[y][x], end="")
    print()
