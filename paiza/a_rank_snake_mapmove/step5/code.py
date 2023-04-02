# https://paiza.jp/works/mondai/a_rank_level_up_problems/a_rank_snake_mapmove_step5
from input2 import _INPUT

def main(*, int=int, input=input):

    directions = ["N", "E", "S", "W"]
    now = 0
    h, w, sy, sx, n = map(int, input().split())
    s = [list(input()) for _ in range(h)]
    s[sy][sx] = "*"
    loop_break = False
    for _ in range(n):
        if loop_break:
            break
        d, c = input().split()
        if d == "R":
            now = (now + 1) % 4
        else:
            now = (now - 1) % 4

        for _ in range(int(c)):
            if directions[now] == "N":
                sy -= 1
            elif directions[now] == "E":
                sx += 1
            elif directions[now] == "S":
                sy += 1
            elif directions[now] == "W":
                sx -= 1

            if sy >= 0 and sx >= 0 and sy < h and sx < w and s[sy][sx] == ".":
                s[sy][sx] = "*"
            else:
                loop_break = True
                break

            # 上記の条件がこれまでの実装と異なるので苦労した
            # 前回までは以下のようにしていた
            # これを利用して実装する方が安定したかもしれない。
            # ただし、条件を逆転させることについて勉強にはなった。
            # if sy < 0 or sx < 0 or sy >= h or sx >= w or s[sy][sx] == "#"

    result = '\n'.join([''.join(row) for row in s])
    print(result)

if __name__ == "__main__":
    import io, sys

    sys.stdin = io.StringIO(_INPUT)

    main()
