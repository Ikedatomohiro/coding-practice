#
from input1 import _INPUT

def main(*, int=int, input=input):
    n, m = map(int, input().split())
    total = 0
    for _ in range(n - 1):
        distance = int(input())
        if distance <= m:
            total += distance

    print(total)

if __name__ == "__main__":
    import io, sys

    sys.stdin = io.StringIO(_INPUT)

    main()
