#
from input2 import _INPUT

def main(*, int=int, input=input):
    n, m = map(int, input().split())
    a, b, c = map(int, input().split())
    close = 0
    dead_line = (a + b * m) / c

    for _ in range(n):
        r = int(input())
        if r < dead_line:
            close += 1
    print(close)

if __name__ == "__main__":
    import io, sys

    sys.stdin = io.StringIO(_INPUT)

    main()
