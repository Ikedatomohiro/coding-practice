#
from input3 import _INPUT

def main(*, int=int, input=input):
    atk, defe ,agi = map(int, input().split())
    n = int(input())
    count = 0
    for _ in range(n):
        s, minatk, maxatk, mindefe, maxdefe, minagi, maxagi = input().split()
        if int(minatk) <= atk <= int(maxatk) and int(mindefe) <= defe <= int(maxdefe) and int(minagi) <= agi <= int(maxagi):
            print(s)
            count += 1
    if count == 0:
        print("no evolution")

if __name__ == "__main__":
    import io, sys

    sys.stdin = io.StringIO(_INPUT)

    main()
