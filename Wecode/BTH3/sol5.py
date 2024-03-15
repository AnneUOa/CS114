import sys
def find_closest_numbers(arr, k, x):
    left = 0
    right = len(arr) - k
    while left < right:
        mid = (left + right) // 2
        if x - arr[mid] > arr[mid + k] - x:
            left = mid + 1
        else:
            right = mid
    return arr[left:left + k]

n = int(sys.stdin.readline())  
arr = list(map(int, sys.stdin.readline().split())) 
arrr = []
while True:
    try:
        k, x = map(int, sys.stdin.readline().split())
        arrr.append([k,x])
    except ValueError:
        break
for a in arrr:
    closest_numbers = find_closest_numbers(arr, a[0], a[1]) 
    print(min(closest_numbers), max(closest_numbers))
