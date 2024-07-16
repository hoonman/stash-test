def binary_search(arr, tar, high, low):
    mid = (high + low) // 2
    if low > high:
        return False
    elif arr[mid] == tar:
        return True
    elif arr[mid] > tar:
        return binary_search(arr, tar, mid - 1, low)
    elif arr[mid] < tar:
        return binary_search(arr, tar, high, mid + 1)

arr = [1,2,3,4,5,6,7,8]
print(binary_search(arr, 1, len(arr) - 1, 0))