# https://paiza.jp/works/mondai/a_rank_level_up_problems/a_rank_camp_step1
from input2 import _INPUT

def main(*, int=int, input=input):
    h, w = map(int, input().split())
    s = [list(input()) for _ in range(h)]
    check = False
    for i in range(h):
        if check:
            break
        for j in range(w):
            if s[i][j] == "*":
                if i - 1 >= 0:
                    s[i - 1][j] = "*"
                if i + 1 < h:
                    s[i +1][j] = "*"
                if j - 1 >= 0:
                    s[i][j - 1] = "*"
                if j + 1 < w:
                    s[i][j + 1] = "*"
                check = True
                break
    for point in s:
        print("".join(point))

if __name__ == "__main__":
    import io, sys

    sys.stdin = io.StringIO(_INPUT)

    main()
