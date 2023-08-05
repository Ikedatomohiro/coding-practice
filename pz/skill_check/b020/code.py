#
from input2 import _INPUT

def main(*, int=int, input=input):
    n = int(input())
    q = [input() for _ in range(n)]
    now = 0
    pages = ["" for _ in range(n + 1)]
    for i in range(n):
        if q[i] == "use the back button":
            print(pages[now - 1])
            now -= 1
        else:
            print(q[i][6:])
            pages[now + 1] = q[i][6:]
            now += 1



if __name__ == "__main__":
    import io, sys

    sys.stdin = io.StringIO(_INPUT)

    main()
