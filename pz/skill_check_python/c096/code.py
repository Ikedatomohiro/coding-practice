#
from input3 import _INPUT
import io, sys
sys.stdin = io.StringIO(_INPUT)

N = int(input())
s_ok = 1
e_ok = 31
for _ in range(N):
    s, e = map(int, input().split())
    # if max(s_ok, s) <= min(e_ok, e):
    if s_ok <= e and e_ok >= s:
        if s_ok < s:
            s_ok = s
        if e_ok > e:
            e_ok = e
    else:
        print("NG")
        exit()
print("OK")
