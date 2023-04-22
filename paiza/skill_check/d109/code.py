#
from input2 import _INPUT

def main(*, int=int, input=input):
    m, d = input().split()
    md = m + d
    first = md[0]
    for i in md[1:]:
        if i != first:
            print("No")
            exit()
    print("Yes")

if __name__ == "__main__":
    import io, sys

    sys.stdin = io.StringIO(_INPUT)

    main()
