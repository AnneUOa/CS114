import sys

n = int(sys.stdin.readline())
a = ( list(reversed(list(map(int, sys.stdin.readline().strip().split())))))
m = int(sys.stdin.readline())
b = list(map(int, sys.stdin.readline().strip().split()))

for i in b:
    try:
        print(len(a) - 1 - a.index(i))
    except:
        print(-1)
