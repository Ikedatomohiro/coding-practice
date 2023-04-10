#
from input1 import _INPUT

def main(*, int=int, input=input):
    n, r = map(int, input().split())
    result = []
    for box, i in enumerate(range(n)):
        h, w, o = map(int, input().split())
        if h >= r * 2 and w >= r * 2 and o >= r * 2:
            result.append(i + 1)
    for i in result:
        print(i)

if __name__ == "__main__":
    import io, sys

    sys.stdin = io.StringIO(_INPUT)

    main()
