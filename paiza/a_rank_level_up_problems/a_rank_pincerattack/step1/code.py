# https://paiza.jp/works/mondai/a_rank_level_up_problems/a_rank_pincerattack_step1
from input2 import _INPUT

def main(*, int=int, input=input):
    H, W, Y, X = map(int, input().split())
    s = [["" for _ in range(W)] for _ in range(H)]
    for y in range(H):
        for x in range(W):
            if y == Y and x == X:
                s[y][x] = "!"
            elif y == Y or x == X:
                s[y][x] = "*"
            else:
                s[y][x] = "."
    for row in s:
        print("".join(row))

if __name__ == "__main__":
    import io, sys

    sys.stdin = io.StringIO(_INPUT)

    main()
