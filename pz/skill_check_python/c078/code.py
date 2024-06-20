#
from input2 import _INPUT

def main(*, int=int, input=input):
    n, c1, c2 = map(int, input().split())
    count = 0
    total = 0
    for _ in range(n):
        p = int(input())
        if p <= c1:
            count += 1
            total -= p
        elif p >= c2:
            total += p * count
            count = 0
    total += p * count
    print(total)

if __name__ == "__main__":
    import io, sys

    sys.stdin = io.StringIO(_INPUT)

    main()
