# https://paiza.jp/works/mondai/a_rank_level_up_problems/a_rank_snake_mapmove_step6
from input2 import _INPUT

def main(*, int=int, input=input):
    h, w, sy, sx, n = map(int, input().split())
    s = [input() for _ in range(h)]
    directions = ["N", "E", "S", "W"]
    now_direction = 0
    time = 0
    now_time = 0
    check = False
    for _ in range(n):
        if check:
            break
        to_time, direction = input().split()
        time = now_time
        for _ in range(int(to_time) - time + 1):
            if int(to_time) == now_time:
                if direction == "L":
                    now_direction = (now_direction - 1) % 4
                else:
                    now_direction = (now_direction + 1) % 4
            if directions[now_direction] == "N":
                sy -= 1
            elif directions[now_direction] == "E":
                sx += 1
            elif directions[now_direction] == "S":
                sy += 1
            elif directions[now_direction] == "W":
                sx -= 1
            if sy < 0 or sx < 0 or sy >= h or sx >= w or s[sy][sx] == "#":
                check = True
                print("Stop")
                break
            print(sy, sx)
            now_time += 1

if __name__ == "__main__":
    import io, sys

    sys.stdin = io.StringIO(_INPUT)

    main()
