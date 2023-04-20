#
from input2 import _INPUT

def main(*, int=int, input=input):
    n = int(input())
    items = list(map(int, input().split()))
    t, q = map(int, input().split())
    for _ in range(q):
        x, k = map(int, input().split())
        amount = items[x - 1] * k
        if t >= amount:
            t -= amount

    print(t)

if __name__ == "__main__":
    import io, sys

    sys.stdin = io.StringIO(_INPUT)

    main()
