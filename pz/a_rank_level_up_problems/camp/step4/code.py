# https://paiza.jp/works/mondai/a_rank_level_up_problems/a_rank_camp_step4
from input2 import _INPUT

def main(*, int=int, input=input):
    from collections import deque
    h, w = map(int, input().split())
    s = [["" for _ in range(w)] for _ in range(h)]
    dist = 0
    for y in range(h):
        row = list(input())
        for x in range(w):
            s[y][x] = row[x]
            if row[x] == "*":
                sy = y
                sx = x

    s[sy][sx] = str(dist)
    dy = (-1, 0, 1, 0)
    dx = (0, 1, 0, -1)
    q = deque()
    q.append((sy, sx, dist))
    while(len(q) > 0):
        y, x, dist = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or ny >= h or nx < 0 or nx >= w or s[ny][nx] == "#":
                continue
            if s[ny][nx] != ".":
                continue
            s[ny][nx] = str(dist + 1)
            q.append((ny, nx, dist + 1))
    for row in s:
        print("".join(row))

if __name__ == "__main__":
    import io, sys

    sys.stdin = io.StringIO(_INPUT)

    main()
