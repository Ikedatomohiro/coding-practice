# https://paiza.jp/works/mondai/a_rank_level_up_problems/a_rank_snake_mapmove_step4
from input1 import _INPUT

directions = ["N", "E", "S", "W"]

def main(*, int=int, input=input):
    h, w, sy, sx, n = map(int, input().split())
    s = [list(input()) for _ in range(h)]
    now = 0

    for _ in range(n):
        d, c = input().split()
        # 向きを変える
        now = change_derection(now, d)
        # 移動する
        for _ in range(int(c)):
            sy, sx, check = move(now, sy, sx, h, w, s)
            if not check:
                print(sy, sx)
                print("Stop")
                exit()
        print(sy, sx)

def change_derection(now, d):
    if d == "L":
        now = (now - 1) % 4
    else:
        now = (now + 1) % 4
    return now

def move(now, sy, sx, h, w, s):
    check = True
    if directions[now] == "N":
        sy -= 1
        if not check_move(sy, sx, h, w, s):
            check = False
            sy += 1
    elif directions[now] == "E":
        sx += 1
        if not check_move(sy, sx, h, w, s):
            check = False
            sx -= 1
    elif directions[now] == "S":
        sy += 1
        if not check_move(sy, sx, h, w, s):
            check = False
            sy -= 1
    elif directions[now] == "W":
        sx -= 1
        if not check_move(sy, sx, h, w, s):
            check = False
            sx += 1
    return sy, sx, check

def check_move(sy, sx, h, w, s):
    check = True
    if sy < 0 or sx < 0 or sy >= int(w) or sx >= int(h) or s[sy][sx] == "#":
        check = False
    return check

if __name__ == "__main__":
    import io, sys

    sys.stdin = io.StringIO(_INPUT)

    main()
