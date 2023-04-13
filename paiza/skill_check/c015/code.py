#
from input1 import _INPUT

def main(*, int=int, input=input):
    import math
    n = int(input())
    point = 0
    for _ in range(n):
        d, p = map(int, input().split())
        if "5" in str(d):
            # ポイントの5％（小数以下は切り捨て）を加算
            point += math.floor(p * 0.05)
        elif "3" in str(d):
            # ポイントの3％（小数以下は切り捨て）を加算
            point += math.floor(p * 0.03)
        else:
            # ポイントの1％（小数以下は切り捨て）を加算
            point += math.floor(p * 0.01)
    print(int(point))

if __name__ == "__main__":
    import io, sys

    sys.stdin = io.StringIO(_INPUT)

    main()
