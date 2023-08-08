#
from input1 import _INPUT, _OUTPUT
import io, sys
sys.stdin = io.StringIO(_INPUT)

H, W = map(int, input().split())

ans = [[0 for j in range(W)] for i in range(H)]

for i in range(H):
    line = map(int, input().split())
    for j, val in enumerate(line):
        if val >= 128:
            ans[i][j] = 1

for i in range(H):
    print(" ".join(map(str, ans[i])))

# 出力を文字列として取得する
output = ""
for i in range(H):
    output += " ".join(map(str, ans[i])) + "\n"

# 出力が期待されるものと一致するかどうかを判定する
if output == _OUTPUT:
    print("OK")
