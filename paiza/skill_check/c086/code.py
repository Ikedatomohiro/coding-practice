#
from input2 import _INPUT

def main(*, int=int, input=input):
    string_list = list(input())
    not_list = ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U" )
    result = ""
    for s in string_list:
        if not s in not_list:
            result += s
    print(result)

if __name__ == "__main__":
    import io, sys

    sys.stdin = io.StringIO(_INPUT)

    main()
