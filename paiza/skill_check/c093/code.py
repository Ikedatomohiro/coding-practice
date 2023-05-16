#
from input3 import _INPUT
import io, sys
sys.stdin = io.StringIO(_INPUT)

X, Y = input().split()
bob = 0
arice = 0
for n in X:
    bob += int(n)

for n in Y:
    arice += int(n)

if str(bob)[-1] == str(arice)[-1]:
    print("Draw")
elif int(str(bob)[-1]) > int(str(arice)[-1]):
    print("Bob")
else:
    print("Alice")