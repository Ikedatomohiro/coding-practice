#
from input1 import _INPUT

def main(*, int=int, input=input):
    k, n = map(int, input().split())
    for _ in range(k):
        point = 0
        d, a = map(int, input().split())
        point = (100 / n) * a
        if 1 <= d <= 9:
            point *= 0.8
        elif 10 <= d:
            point = 0
        # ポイントの少数以下は切り捨て
        point = int(point)
        print(point)
        if point >= 80:
            print("A")
        elif point >= 70:
            print("B")
        elif point >= 60:
            print("C")
        else:
            print("D")

if __name__ == "__main__":
    import io, sys

    sys.stdin = io.StringIO(_INPUT)

    main()
