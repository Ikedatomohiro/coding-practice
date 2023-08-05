#
from input1 import _INPUT
import io, sys
sys.stdin = io.StringIO(_INPUT)

import re
N = int(input())
ans = {}
list = []
for _ in range(N):
    id = input()
    match = re.search(r'\d', id)
    index = match.start()
    number = id[index:]
    list.append(int(number))
    ans[int(number)] = id

list.sort()
for i in list:
    print(ans[i])
