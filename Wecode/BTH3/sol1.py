import sys

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            if mid == len(arr) - 1 or arr[mid + 1] != target:
                return mid
            else:
                left = mid + 1
        elif arr[mid] < target:
            right = mid - 1
        else:
            left = mid + 1
    return -1

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))[::-1]
m = int(sys.stdin.readline())
b = list(map(int, sys.stdin.readline().split()))

for target in b:
    idx = binary_search(a, target)
    if idx != -1:
        print(n - 1 - idx)
    else:
        print(-1)
