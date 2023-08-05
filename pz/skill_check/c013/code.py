#
from input2 import _INPUT

def main(*, int=int, input=input):
    n = input()
    m = int(input())
    result = []
    for _ in range(m):
        r = input()
        if n in r:
            continue
        result.append(r)

    for r in result:
        print(r)
    if result == []:
        print("none")

if __name__ == "__main__":
    import io, sys

    sys.stdin = io.StringIO(_INPUT)

    main()
