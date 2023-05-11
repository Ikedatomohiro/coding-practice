#
from input1 import _INPUT
import io, sys
sys.stdin = io.StringIO(_INPUT)

N = input()
H = int(len(N))
s = [["." for _ in range(9)] for _ in range(H)]
# print(0 // 3)
# print(((2 - 1) % 3) * 3)
for i in range(H):
    # print(i)
    number = int(N[i])
    # print(number, int(i) // 3)
    sy = ((int(i)) // 3) * 3
    sx = ((int(i)) % 3) * 3
    for y in range(sy, sy + 3):
        for x in range(sx, sx + 3):
            # print(y, x, "----")
            if number > 0:
                s[y][x] = "#"
                number -= 1
    # for row in s:
    #     print("".join(row))
    # if i == 2:
    #     exit()
#     l = (int(i) // 3) * 3
#     for k in range(j, j + 3):
#         s[j + l][k] = "#"
    # print(i)

# # print(H)
for row in s:
    print("".join(row))