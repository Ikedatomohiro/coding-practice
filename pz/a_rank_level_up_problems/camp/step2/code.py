# https://paiza.jp/works/mondai/a_rank_level_up_problems/a_rank_camp_step2
from input2 import _INPUT

def main(*, int=int, input=input):
    h, w = map(int, input().split())
    s = [list(input()) for _ in range(h)]
    check = False
    for y in range(h):
        if check:
            break
        for x in range(w):
            if s[y][x] == "*":
                if y > 0 and s[y - 1][x] == ".":
                    s[y - 1][x] = "*"
                if y < h - 1 and s[y + 1][x] == ".":
                    s[y + 1][x] = "*"
                if x > 0 and s[y][x - 1] == ".":
                    s[y][x - 1] = "*"
                if x < w - 1 and s[y][x + 1] == ".":
                    s[y][x + 1] = "*"
                check = True
                break
    for row in s:
        print("".join(row))


if __name__ == "__main__":
    import io, sys

    sys.stdin = io.StringIO(_INPUT)

    main()
