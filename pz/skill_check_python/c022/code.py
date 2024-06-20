#
from input2 import _INPUT

def main(*, int=int, input=input):
    n = int(input())
    for i in range(n):
        s, e, h, l = map(int, input().split())
        if i == 0:
            hajime = s
            owari = e
            saitaka = h
            saiyasu = l
        if i == n - 1:
            owari = e
        if saiyasu > l:
            saiyasu = l
        if saitaka < h:
            saitaka = h
    print(hajime, owari, saitaka, saiyasu)
if __name__ == "__main__":
    import io, sys

    sys.stdin = io.StringIO(_INPUT)

    main()
