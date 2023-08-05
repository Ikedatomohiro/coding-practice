# https://paiza.jp/works/mondai/a_rank_level_up_problems/a_rank_pincerattack_step3
from input2 import _INPUT

def main(*, int=int, input=input):
    H, W, Y, X = map(int, input().split())
    s = [["" for _ in range(W)] for _ in range(H)]
    for y in range(H):
        for x in range(W):
            s[y][x] = "."
    dy = (-1, -1, 1, 1)
    dx = (-1, 1, -1, 1)
    s[Y][X] = "!"
    for i in range(4):
        ny = Y
        nx = X
        while True:
            ny += dy[i]
            nx += dx[i]
            if ny < 0 or ny >= H or nx < 0 or nx >= W:
                break
            if s[ny][nx] == ".":
                s[ny][nx] = "*"
    for row in s:
        print("".join(row))

    # 別解
    # 石を置いた場所と斜めのマスを満たす条件は、X軸、Y軸の差が等しいこと
    H, W, Y, X = map(int, input().split())
    for i in range(H):
        for j in range(W):
            if i == Y and j == X:
                print("!", end="")
            elif abs(i - Y) == abs(j - X):
                print("*", end="")
            else:
                print(".", end="")
        print()

if __name__ == "__main__":
    import io, sys

    sys.stdin = io.StringIO(_INPUT)

    main()
