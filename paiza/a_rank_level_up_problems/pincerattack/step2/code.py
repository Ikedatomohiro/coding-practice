# https://paiza.jp/works/mondai/a_rank_level_up_problems/a_rank_pincerattack_step2
from input2 import _INPUT

def main(*, int=int, input=input):
    H, W, Y, X = map(int, input().split())
    s = [list(input()) for _ in range(H)]
    dy = (-1, 0, 1, 0)
    dx = (0, 1, 0, -1)
    rebers = []
    check = False
    for i in range(4):
        ny, nx = Y, X
        while True:
            ny += dy[i]
            nx += dx[i]
            if ny < 0 or ny >= H or nx < 0 or nx >= W:
                break
            if s[ny][nx] == "*":
                check = True
                break
            if s[ny][nx] == ".":
                rebers.append((ny, nx))
        if check:
            for y, x in rebers:
                s[y][x] = "*"
            rebers = []
            check = False

    s[Y][X] = "*"
    for row in s:
        print("".join(row))

if __name__ == "__main__":
    import io, sys

    sys.stdin = io.StringIO(_INPUT)

    main()
