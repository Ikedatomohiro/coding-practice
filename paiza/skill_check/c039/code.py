#
from input1 import _INPUT

def main(*, int=int, input=input):
    kihou = input()
    result = 0
    for moji in kihou:
        if moji == '/':
            result += 1
        elif moji == '<':
            result += 10

    print(result)

if __name__ == "__main__":
    import io, sys

    sys.stdin = io.StringIO(_INPUT)

    main()
