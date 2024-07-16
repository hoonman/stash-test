def binary_search(arr, target, high, low):
    mid = (high + low) // 2
    if low > high:
        return False
    elif arr[mid] == target:
        return True
    elif arr[mid] > target:
        return binary_search(arr, target, mid - 1, low)
    elif arr[mid] < target:
        return binary_search(arr, target, high, mid + 1)

arr = [1,2,3,4,5,6,7,8]
print(binary_search(arr, 1, len(arr) - 1, 0))