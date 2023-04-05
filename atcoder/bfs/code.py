#
from input1 import _INPUT
from collections import deque

def main(*, int=int, input=input):
    r, c = map(int, input().split())
    sy, sx = map(lambda x: int(x) - 1, input().split())
    gy, gx = map(lambda x: int(x) - 1, input().split())

    grid = [input() for _ in range(r)]
    q = deque()
    q.append((sy, sx))
    INF = -1 # 1 << 60 # 1: 0001 1<<3: 1000 ビットシフトの書き方
    dist = [[INF for _ in range(c)] for _ in range(r)]
    dist[sy][sx] = 0

    dy = (0, 1, 0, -1)
    dx = (1, 0, -1, 0)
    while(len(q) > 0):
        now = q.popleft()
        y, x = now
        for di in range(4):
            ny = y + dy[di]
            nx = x + dx[di]

            if ny < 0 or ny >= r or nx < 0 or nx >= c or grid[ny][nx] == "#":
                continue
            if dist[ny][nx] != INF:
                continue

            dist[ny][nx] = dist[y][x] + 1
            q.append((ny, nx))
    print(dist[gy][gx])

if __name__ == "__main__":
    import io, sys

    sys.stdin = io.StringIO(_INPUT)

    main()
