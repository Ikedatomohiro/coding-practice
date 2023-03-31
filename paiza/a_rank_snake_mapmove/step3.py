# https://paiza.jp/works/mondai/a_rank_level_up_problems/a_rank_snake_mapmove_step3
_INPUT = """\
7 11 1 5 43
.##........
.#......##.
.#....#...#
.###......#
#......###.
..#....###.
#.#........
L
L
R
L
R
L
R
L
L
R
L
R
L
L
L
L
R
R
R
L
R
L
R
L
L
R
L
L
R
L
R
L
R
R
R
R
L
R
L
L
L
R
R
"""

def main(*, int=int, input=input):
    h, w, sy, sx, n = map(int, input().split())
    directions = ["N", "E", "S", "W"]
    now = 0
    s = [list(input()) for _ in range(h)]

    for _ in range(n):
        # 向きを変える
        if input() == "L":
            now = (now - 1) % 4
        else:
            now = (now + 1) % 4

        # 一歩進む
        if directions[now] == "N":
            sy -= 1        
        elif directions[now] == "E":
            sx += 1
        elif directions[now] == "S":
            sy += 1
        elif directions[now] == "W":
            sx -= 1
        
        # 結果を出力
        if sy < 0 or sy >= h or sx < 0 or sx >= w or s[sy][sx] == "#":
            print("Stop")
            break
        else:
            print(sy, sx)


if __name__ == "__main__":
    import io, sys

    sys.stdin = io.StringIO(_INPUT)
    
    main()

    