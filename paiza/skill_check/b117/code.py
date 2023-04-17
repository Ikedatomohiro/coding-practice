#
from input3 import _INPUT

def main(*, int=int, input=input):
    n = int(input())
    cars = [int(input()) for _ in range(n)]
    cycle = 0
    for i in range(n - 1):
        if cars[i] > cars[i + 1]:
            cycle += 1
    print(cycle)

if __name__ == "__main__":
    import io, sys

    sys.stdin = io.StringIO(_INPUT)

    main()
