#
from input1 import _INPUT

def main(*, int=int, input=input):
    import math
    n, q = map(int, input().split())
    s = input()
    for _ in range(q):
        l, r = map(int, input().split())
        t = s[l - 1:r]
        diff_line = 0
        for i in range(r - l):
            if t[i] != t[i + 1]:
                diff_line += 1

        result = math.ceil(diff_line / 2)
        print(result)

if __name__ == "__main__":
    import io, sys

    sys.stdin = io.StringIO(_INPUT)

    main()
