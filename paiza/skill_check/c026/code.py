#
from input2 import _INPUT

def main(*, int=int, input=input):
    N, S, p = map(int, input().split())
    W = 0
    index = 0
    for i in range(N):
        m, s = map(int, input().split())
        if S - p <= s <= S + p:
            if W < m:
                W = m
                index = i + 1
    if index == 0:
        print("not found")
    else:
        print(index)

if __name__ == "__main__":
    import io, sys

    sys.stdin = io.StringIO(_INPUT)

    main()
