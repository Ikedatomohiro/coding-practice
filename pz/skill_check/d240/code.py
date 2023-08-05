#
from input1 import _INPUT

def main(*, int=int, input=input):
    name = input()
    result = name + "A"
    print(result)

if __name__ == "__main__":
    import io, sys

    sys.stdin = io.StringIO(_INPUT)

    main()
