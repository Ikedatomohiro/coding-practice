# https://paiza.jp/works/mondai/a_rank_level_up_problems/a_rank_snake_mapmove_boss
from input2 import _INPUT

def main(*, int=int, input=input):
    h, w, sy, sx, n = map(int, input().split())
    directins = ["N", "E", "S", "W"]
    now = 0
    s = [list(input()) for _ in range(h)]
    time_lr = [input().split() for _ in range(n)]
    s[sy][sx] = "*"
    time = 0

    for t_now in range(100):
        if time < n and str(t_now) == time_lr[time][0]:
            d = time_lr[time][1]
            time += 1
            if d == "L":
                now = (now - 1) % 4
            else:
                now = (now + 1) % 4
        if directins[now] == "N":
            sy -= 1
        elif directins[now] == "E":
            sx += 1
        elif directins[now] == "S":
            sy += 1
        elif directins[now] == "W":
            sx -= 1
        if sy < 0 or sx < 0 or sy >= h or sx >= w or s[sy][sx] != ".":
            break
        else:
            s[sy][sx] = "*"

    for row in s:
        print("".join(row))

if __name__ == "__main__":
    import io, sys

    sys.stdin = io.StringIO(_INPUT)

    main()
