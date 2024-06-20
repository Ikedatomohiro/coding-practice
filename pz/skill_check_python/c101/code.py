#
from input2 import _INPUT
import re
def main(*, int=int, input=input):
    count = 0
    x = input()
    for i in range(365):
        result = re.search(x, str(i))
        if result:
            count += 1
    print(count)

if __name__ == "__main__":
    import io, sys

    sys.stdin = io.StringIO(_INPUT)

    main()
