# https://paiza.jp/works/mondai/a_rank_level_up_problems/a_rank_camp_step3
from input1 import _INPUT

def main(*, int=int, input=input):
    from collections import deque
    h, w = map(int, input().split())
    s = [["" for _ in range(w)] for _ in range(h)]
    for y in range(h):
        row = list(input())
        for x in range(w):
            s[y][x] = row[x]
            if row[x] == "*":
                sy = y
                sx = x
    # 上、右、下、左に移動を想定
    dy = (-1, 0, 1, 0)
    dx = (0, 1, 0, -1)
    dist = [[-1 for _ in range(w)] for _ in range(h)]
    dist[sy][sx] = 1
    q = deque()
    q.append((sy, sx))
    while(len(q) > 0):
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or ny >= h or nx < 0 or nx >= w or s[ny][nx] == "#":
                continue
            if dist[ny][nx] != -1:
                continue
            dist[ny][nx] = 1
            s[ny][nx] = "*"
            q.append((ny, nx))

    for row in s:
        print("".join(row))

if __name__ == "__main__":
    import io, sys

    sys.stdin = io.StringIO(_INPUT)

    main()
