# https://paiza.jp/works/mondai/bfs_dfs_problems/bfs_dfs_problems__move_once
from input2 import _INPUT

def main(*, int=int, input=input):
    h, w = map(int, input().split())
    y, x = map(int, input().split())

    s = [["." for _ in range(w)] for _ in range(h)]
    s[y][x] = "*"
    if y - 1 >= 0:
        s[y - 1][x] = "*"
    if y + 1 < h:
        s[y + 1][x] = "*"
    if x - 1 >= 0:
        s[y][x - 1] = "*"
    if x + 1 < w:
        s[y][x + 1] = "*"
    for row in s:
        print("".join(row))


if __name__ == "__main__":
    import io, sys

    sys.stdin = io.StringIO(_INPUT)

    main()
