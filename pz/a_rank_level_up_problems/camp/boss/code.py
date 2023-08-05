# https://paiza.jp/works/mondai/a_rank_level_up_problems/a_rank_camp_boss
from input2 import _INPUT

def main(*, int=int, input=input):
    from collections import deque
    h, w = map(int, input().split())
    # 最初に行動するプレイヤー
    f = input()
    s = ""
    if f == "A":
        s = "B"
    else:
        s = "A"
    grid = [["" for _ in range(h)] for _ in range(w)]
    for y in range(h):
        row = list(input())
        for x in range(w):
            grid[y][x] = row[x]
            # 最初に行動するプレイヤーの位置
            if row[x] == f:
                sfy = y
                sfx = x
                grid[sfy][sfx] = "F"
            # 2番目に行動するプレイヤーの位置
            elif (row[x] == "A" or row[x] == "B") and row[x] != f:
                ssy = y
                ssx = x
                grid[ssy][ssx] = "S"

    dy = (-1, 0, 1, 0)
    dx = (0, 1, 0, -1)
    qf = deque()
    qs = deque()
    f_count = 1
    s_count = 1
    qf.append((sfy, sfx))
    qs.append((ssy, ssx))

    while(len(qf) > 0 or len(qs) > 0):
        if len(qf) > 0:
            q = qf
            qf = deque()
            while len(q) > 0:
                y, x = q.popleft()
                for i in range(4):
                    ny = y + dy[i]
                    nx = x + dx[i]
                    if ny < 0 or ny >= h or nx < 0 or nx >= w:
                        continue
                    if grid[ny][nx] != ".":
                        continue
                    grid[ny][nx] = "F"
                    f_count += 1
                    qf.append((ny, nx))

        if len(qs) > 0:
            q = qs
            qs = deque()
            while len(q) > 0:
                y, x = q.popleft()
                for i in range(4):
                    ny = y + dy[i]
                    nx = x + dx[i]
                    if ny < 0 or ny >= h or nx < 0 or nx >= w:
                        continue
                    if grid[ny][nx] != ".":
                        continue
                    grid[ny][nx] = "S"
                    s_count += 1
                    qs.append((ny, nx))

    if f == "A":
        print(f_count, s_count)
    else:
        print(s_count, f_count)
    if f_count > s_count:
        print(f)
    else:
        print(s)

if __name__ == "__main__":
    import io, sys

    sys.stdin = io.StringIO(_INPUT)

    main()
