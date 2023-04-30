# https://paiza.jp/works/mondai/a_rank_level_up_problems/a_rank_pincerattack_step4
from input2 import _INPUT

def main(*, int=int, input=input):
    H, W, Y, X = map(int, input().split())
    s = [list(input()) for _ in range(H)]
    s[Y][X] = "*"
    dy = (-1, -1, 1, 1)
    dx = (-1, 1, -1, 1)
    for i in range(4):
        reverse = []
        ny = Y
        nx = X
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

    for row in s:
        print("".join(row))

if __name__ == "__main__":
    import io, sys

    sys.stdin = io.StringIO(_INPUT)

    main()
