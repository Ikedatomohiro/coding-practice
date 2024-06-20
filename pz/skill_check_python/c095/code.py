#
from input2 import _INPUT

def main(*, int=int, input=input):
    s = input()
    t = input()
    if s == t:
        print("NO")
    else:
        string = t
        for i in s:
            if i in string:
                string = string.replace(i, "", 1)
            else:
                print("NO")
                exit()
        print("YES")

if __name__ == "__main__":
    import io, sys

    sys.stdin = io.StringIO(_INPUT)

    main()
