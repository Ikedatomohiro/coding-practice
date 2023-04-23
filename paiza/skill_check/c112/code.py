#
from input2 import _INPUT

def main(*, int=int, input=input):
    n = int(input())
    max = 0
    min = 0
    for i in range(n):
        s, f, t = map(int, input().split())
        hours = s + f + 24 - t
        if i == 0:
            max = hours
            min = hours
        if hours > max:
            max = hours
        if hours < min:
            min = hours
    print(min)
    print(max)

if __name__ == "__main__":
    import io, sys

    sys.stdin = io.StringIO(_INPUT)

    main()
